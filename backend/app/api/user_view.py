from flask.views import MethodView
from flask import request, jsonify
from app.models import User
from app.extensions import db
from app.schemas.user_schema import UsersSchema
from marshmallow import ValidationError

user_schema = UsersSchema()
user_list_schema = UsersSchema(many=True)

class UserAPI(MethodView):
    def get(self, user_id=None):
        """Get all users or a specific user by ID"""
        if user_id is None:
            users = User.query.all()
            result = user_list_schema.dump(users)
            return jsonify(result), 200

        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404

        result = user_schema.dump(user)
        return jsonify(result), 200

    def post(self):
        """Create a new user"""
        data = request.get_json()
        try:
            valid_data = user_schema.load(data)
        except ValidationError as err:
            return jsonify(err.messages), 400

        new_user = User(
            name=valid_data['name'],
            email=valid_data['email'],
            password=valid_data['password'],
            phone=valid_data['phone']
        )

        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User created success'})

