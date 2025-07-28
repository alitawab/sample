"""cart service"""
from app.models.cart import Cart
from app.extensions import db


def get_all_carts():
    """get all cart"""
    return Cart.query.all()

def get_cart(cart_id):
    """get cart"""
    return Cart.query.get(cart_id)

def create_cart(data):
    """create cart"""
    cart = Cart(**data)
    db.session.add(cart)
    db.session.commit()
    return cart

def update_cart(cart, data):
    """update cart"""
    for key, value in data.items():
        setattr(cart, key, value)
    db.session.commit()
    return cart

def delete_cart(cart):
    """delete cart"""
    db.session.delete(cart)
    db.session.commit()
