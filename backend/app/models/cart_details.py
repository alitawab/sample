"""model cart details"""
from app.extensions import db

class CartDetails(db.Model):
    """class for cart details model"""
    __tablename__ = 'cart_details'

    cartdetails_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.cart_id'), nullable=False)
    menuitem_id = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.String(45), nullable=False)

    # Relationship to cart
    cart = db.relationship('Cart', backref=db.backref('cart_details', lazy=True))
