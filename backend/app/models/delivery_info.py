from app.extensions import db

class DeliveryInfo(db.Model):
    __tablename__ = 'delivery_info'

    deliveryinfo_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rider_id = db.Column(db.Integer, db.ForeignKey('rider.rider_id', onupdate='RESTRICT'), nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey('order.order_id', onupdate='RESTRICT'), nullable=False)
    pickup_time = db.Column(db.DateTime, nullable=False)
    delivery_time = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(45), nullable=False)

    # Relationships (assuming 'Rider' and 'Order' models exist)
    rider = db.relationship('Rider', backref=db.backref('delivery_infos', lazy=True))
    order = db.relationship('Order', backref=db.backref('delivery_info', uselist=False))
