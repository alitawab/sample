"""user authentication routes"""
from datetime import timedelta
from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

from app.schemas.user_schema import UsersSchema
from app.extensions import db
from app.models import User

auth_bp = Blueprint("auth", __name__)
user_schema = UsersSchema()

@auth_bp.route("/register", methods=["POST"])
def register():
    """function for user register"""
    data = request.get_json()

    try:
        valid_data = user_schema.load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    if User.query.filter_by(email=valid_data["email"]).first():
        return jsonify({"error": "Email already registered"}), 400

    hashed_password = generate_password_hash(valid_data["password"])

    new_user = User(
        name=valid_data["name"],
        email=valid_data["email"],
        password=hashed_password,
        phone=valid_data["phone"]
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201


@auth_bp.route("/login", methods=["POST"])
def login():
    """function for user login"""
    data = request.get_json()

    user = User.query.filter_by(email=data.get("email")).first()
    if not user or not check_password_hash(user.password, data.get("password")):
        return jsonify({"error": "Invalid email or password"}), 401

    access_token = create_access_token(identity=user.user_id, expires_delta=timedelta(days=1))
    return jsonify({"access_token": access_token}), 200
