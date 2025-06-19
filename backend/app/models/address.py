"""mixin file for schema"""
from app.extensions import db

class Address(db.Model):
    """class for table address"""

    __tablename__ = 'address'

    address_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'user.user_id', ondelete='RESTRICT', onupdate='RESTRICT'),
        nullable=False)
    street = db.Column(db.String(45), nullable=False)
    city = db.Column(db.String(45), nullable=False)
    state = db.Column(db.String(45), nullable=False)
    zip_code = db.Column(db.String(45), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

    # Relationship (optional if User model exists)
    user = db.relationship('User', backref=db.backref('addresses', lazy=True))
