"""menu item model"""
from app.extensions import db


class MenuItem(db.Model):
    """menu item function"""
    __tablename__ = 'menu_item'

    menuitem_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    resturant_id = db.Column(db.Integer, db.ForeignKey('resturant.resturant_id'), nullable=False)
    name = db.Column(db.String(45), nullable=False)
    description = db.Column(db.String(45), nullable=False)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(45), nullable=False)
    is_available = db.Column(db.Boolean, nullable=False)

    # Relationship to restaurant
    resturant = db.relationship('Resturant', backref=db.backref('menu_items', lazy=True))
