from app.extensions import db





class OrderDetails(db.Model):
    """class for table order_details"""

    __tablename__ = 'order_details'

    orderdetails_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.order_id'), nullable=False)
    menuitem_id = db.Column(db.Integer, db.ForeignKey('menu_item.menuitem_id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Float, nullable=False)

    # Relationships
    order = db.relationship('Order', backref=db.backref('order_details', lazy=True))
    menu_item = db.relationship('MenuItem', backref=db.backref('order_details', lazy=True))

