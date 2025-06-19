"""user routes"""
from flask import Blueprint, request, jsonify
from app.models import User
from app.extensions import db

user_bp = Blueprint('user', __name__)

@user_bp.route('/', methods=['GET'])
def get_user():
    """function get all user"""
    users = User.query.all()
    return jsonify([{
        'user_id':user.user_id,
        'name':user.name,
        'email':user.email,
        'password':user.password,
        'phone':user.phone,

    } for user in  users ]), 200

@user_bp.route('/',methods=['POST'])
def create_user():
    """function to create new user"""
    data = request.get_json()
    new_user = User (
        name = data['name'],
        email = data['email'],
        password = data['password'],
        phone = data['phone']

    )
    db.session.add(new_user)
    return jsonify({'message':'user created successfuly'}),201
