from app.extensions import db


class CartDetails(db.Model):
    __tablename__ = 'cart_details'

    cartdetails_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.cart_id'), nullable=False)
    menuitem_id = db.Column(db.Integer, nullable=False)  # We'll connect this to the menu item model later
    quantity = db.Column(db.String(45), nullable=False)

    # Relationship to cart
    cart = db.relationship('Cart', backref=db.backref('cart_details', lazy=True))
