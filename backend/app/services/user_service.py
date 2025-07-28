"""User service"""
from app.models.user import User
from app.extensions import db


def get_all_users():
    """get all user"""
    return User.query.all()

def get_user(user_id):
    """get user"""
    return User.query.get(user_id)

def create_user(data):
    """create user"""
    user = User(**data)
    db.session.add(user)
    db.session.commit()
    return user

def update_user(user, data):
    """update user"""
    for key, value in data.items():
        setattr(user, key, value)
    db.session.commit()
    return user

def delete_user(user):
    """delete user"""
    db.session.delete(user)
    db.session.commit()
