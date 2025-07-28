"""order_details service"""
from app.models.order_details import OrderDetails
from app.extensions import db


def get_all_order_details():
    """get all order_details"""
    return OrderDetails.query.all()

def get_order_details(order_details_id):
    """get order_details"""
    return OrderDetails.query.get(order_details_id)

def create_order_details(data):
    """create order_details"""
    order_details = OrderDetails(**data)
    db.session.add(order_details)
    db.session.commit()
    return order_details

def update_order_details(order_details, data):
    """update order_details"""
    for key, value in data.items():
        setattr(order_details, key, value)
    db.session.commit()
    return order_details

def delete_order_details(order_details):
    """delete order_details"""
    db.session.delete(order_details)
    db.session.commit()
