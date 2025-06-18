from app.extensions import db

class Rider(db.Model):
    """class for table rider"""
    
    __tablename__ = 'rider'

    rider_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    phone = db.Column(db.String(45), nullable=False)
    vehicle_type = db.Column(db.String(45), nullable=False)
    current_location_lat = db.Column(db.Float, nullable=False)
    current_location_lng = db.Column(db.Float, nullable=False)
    is_available = db.Column(db.Boolean, nullable=False)

    # Relationships
    delivery_infos = db.relationship('DeliveryInfo', backref='rider', lazy=True)
    orders = db.relationship('Order', backref='rider', lazy=True)
