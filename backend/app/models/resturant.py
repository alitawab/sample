"""model for resturant"""
from app.extensions import db


class Resturant(db.Model):
    """class for table resturant"""

    __tablename__ = 'resturant'  # Keeping the table name as-is for now

    resturant_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"))
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    logo_url = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    tags = db.Column(db.String(255), nullable=True)
    open_hours = db.Column(db.String(255), nullable=False)

    # Relationships (used in: Order, MenuItem)
    user = db.relationship("User", back_populates="resturant")
    orders = db.relationship('Order', backref='resturant', lazy=True)
