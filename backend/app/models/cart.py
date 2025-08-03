"""model cart"""
from app.extensions import db


class Cart(db.Model):
    """function for cart"""
    __tablename__ = 'cart'

    cart_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id', onupdate='RESTRICT'), nullable=True)
    guest_token = db.Column(db.String(255), unique=True, nullable=True)
    status = db.Column(db.String(255), nullable=False)
    

    # Relationship to User (optional but recommended)
    user = db.relationship('User', backref=db.backref('carts', lazy=True))
