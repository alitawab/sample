"""user view module"""
from datetime import timedelta
import os
from flask.views import MethodView
from flask import request, jsonify
from marshmallow import ValidationError
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from app.schemas.user_schema import UsersSchema
from app.extensions import db
from app.models.user import User
from app.models.resturant import Resturant
from app.models.rider import Rider

user_schema = UsersSchema()
user_list_schema = UsersSchema(many=True)

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'app', 'static', 'uploads','resturants')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

class LoginAPI(MethodView):
    """User login API"""
    def post(self):
        """function for user login"""
        data = request.get_json()
        user = User.query.filter_by(email=data.get("email")).first()
        if not user or not check_password_hash(user.password, data.get("password")):
            return jsonify({"error": "Invalid email or password"}), 401

        access_token = create_access_token(identity=user.user_id, expires_delta=timedelta(days=1))
        return jsonify({
            "token": access_token,
            "user": user_schema.dump(user)
            }), 200

class RegisterAPI(MethodView):
    """User Registration Api"""
    def post(self):
        """function for register user"""
        data = request.form.to_dict()
        image = request.files.get('image')

        if image:
            filename = secure_filename(image.filename)
            image_path = os.path.join(UPLOAD_FOLDER,filename)
            image.save(image_path)
            image_url = f'/static/uploads/resturants/{filename}'
        else:
            image_url = ''
            
        user_data = {
            "name":data.get("name"),
            "email":data.get("email"),
            "phone":data.get("phone"),
            "password":data.get("password"),
            "role":data.get("role")
        }

        try:
            valid_data = user_schema.load(user_data)
        except ValidationError as err:
            return jsonify(err.messages), 400

        if User.query.filter_by(email=valid_data["email"]).first():
            return jsonify({"error": "Email already registered"}), 400

        hashed_password = generate_password_hash(valid_data["password"])
        new_user = User(
            name=valid_data["name"],
            email=valid_data["email"],
            password=hashed_password,
            phone=valid_data["phone"],
            role=valid_data["role"]
        )
        print(valid_data)
        db.session.add(new_user)
        db.session.commit()


        if new_user.role == 'resturant':
            resturant = Resturant (
                user_id=new_user.user_id,
                name=data.get("resturant_name"),
                address=data.get("resturant_address"),
                logo_url=image_url,
                phone=new_user.phone,
                rating=0.0,
                tags=data.get("tags"),
                open_hours=data.get("open_hours"),
                )
            print(resturant)
            db.session.add(resturant)
            db.session.commit()
            return jsonify({"message": "Resturant registered successfully"}), 201

        if new_user.role == 'rider':
            rider = Rider (
                name="Sample",
                phone="Sample",
                vehicle_type="Sample",
                current_location_lat=0.0,
                current_location_lng=0.0,
                is_available=True,
                )
            db.session.add(rider)
            db.session.commit()
            return jsonify({"message": "Rider registered successfully"}), 201


        return jsonify({"message": "User registered successfully"}), 201
