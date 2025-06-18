from app.extensions import db


class Order(db.Model):
    __tablename__ = 'order'

    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey('address.address_id'), nullable=False)
    rider_id = db.Column(db.Integer, db.ForeignKey('rider.rider_id'), nullable=True)
    resturant_id = db.Column(db.Integer, db.ForeignKey('resturant.resturant_id'), nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(45), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    # Relationships
    user = db.relationship('User', backref=db.backref('orders', lazy=True))
    address = db.relationship('Address', backref=db.backref('orders', lazy=True))
    rider = db.relationship('Rider', backref=db.backref('orders', lazy=True))
    resturant = db.relationship('Resturant', backref=db.backref('orders', lazy=True))
