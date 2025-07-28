"""cart_detail service"""
from app.models.cart_details import CartDetails
from app.extensions import db


def get_all_cart_details():
    """get all cart_detail"""
    return CartDetails.query.all()

def get_cart_detail(cart_detail_id):
    """get cart_detail"""
    return CartDetails.query.get(cart_detail_id)

def create_cart_detail(data):
    """create cart_detail"""
    cart_detail = CartDetails(**data)
    db.session.add(cart_detail)
    db.session.commit()
    return cart_detail

def update_cart_detail(cart_detail, data):
    """update cart_detail"""
    for key, value in data.items():
        setattr(cart_detail, key, value)
    db.session.commit()
    return cart_detail

def delete_cart_detail(cart_detail):
    """delete cart_detail"""
    db.session.delete(cart_detail)
    db.session.commit()
