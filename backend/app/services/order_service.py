"""order service"""
from app.models.order import Order
from app.extensions import db


def get_all_orders():
    """get all order"""
    return Order.query.all()

def get_order(order_id):
    """get order"""
    return Order.query.get(order_id)

def create_order(data):
    """create order"""
    order = Order(**data)
    db.session.add(order)
    db.session.commit()
    return order

def update_order(order, data):
    """update order"""
    for key, value in data.items():
        setattr(order, key, value)
    db.session.commit()
    return order

def delete_order(order):
    """delete order"""
    db.session.delete(order)
    db.session.commit()
