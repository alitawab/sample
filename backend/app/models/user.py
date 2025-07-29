"""user model"""
from app.extensions import db


class User(db.Model):
    """class for table user"""

    __tablename__ = 'user'  # Using capitalized table name as per your schema

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(255), nullable=False)
