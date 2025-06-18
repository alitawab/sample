from app.extensions import db


class Resturant(db.Model):
    """class for table resturant"""
    
    __tablename__ = 'resturant'  # Keeping the table name as-is for now

    resturant_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    address = db.Column(db.String(45), nullable=False)
    logo_url = db.Column(db.String(45), nullable=False)
    phone = db.Column(db.String(45), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    open_hours = db.Column(db.String(45), nullable=False)

    # Relationships (used in: Order, MenuItem)
    menu_items = db.relationship('MenuItem', backref='resturant', lazy=True)
    orders = db.relationship('Order', backref='resturant', lazy=True)
