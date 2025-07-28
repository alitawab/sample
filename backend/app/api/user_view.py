"""user view module"""
from flask.views import MethodView
from flask import request, jsonify
from marshmallow import ValidationError

from app.schemas.user_schema import UsersSchema
from app.services.user_service import (
    get_all_users, get_user, create_user, update_user, delete_user
    )

user_schema = UsersSchema()
user_list_schema = UsersSchema(many=True)

class UserAPI(MethodView):
    """view module class"""
    def get(self, user_id=None):
        """Get all users or a specific user by ID"""
        if user_id:
            user = get_user(user_id)
            if not user:
                return jsonify({'error': 'User not found'}), 404
            return user_schema.dump(user),200
        users = get_all_users()
        return user_schema.dump(users), 200

    def post(self):
        """Create a new user"""
        data = request.get_json()
        try:
            valid_data = user_schema.load(data)
        except ValidationError as err:
            return jsonify(err.messages), 400

        user = create_user(valid_data)
        return user_schema.dump(user), 201

    def put(self, user_id):
        """update user"""
        user = get_user(user_id)
        if not user:
            return jsonify({'error':'user not found'}), 404

        data = user_schema.load(request.json(), partial=True)
        user= update_user(user, data)
        return user_schema.dump(user), 200

    def delete(self, user_id):
        """delete user"""
        user = get_user(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404

        delete_user(user)
        return '', 204
