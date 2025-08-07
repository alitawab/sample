from app.extensions import db

class Rider(db.Model):
    """class for table rider"""

    __tablename__ = 'rider'

    rider_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(255), nullable=False)
    vehicle_type = db.Column(db.String(255), nullable=False)
    license_number = db.Column(db.String(255), nullable=True)
    current_location_lat = db.Column(db.Float, nullable=False)
    current_location_lng = db.Column(db.Float, nullable=False)
    is_available = db.Column(db.Boolean, nullable=False)

    # Relationships
    orders = db.relationship('Order', backref='rider', lazy=True)
    user = db.relationship('User', backref='rider', lazy=True)
