"""cart service"""
from app.models.cart import Cart
from app.models.cart_details import CartDetails
from app.extensions import db

def get_user_or_guest_cart(user_id,guest_token):
    """function for getting cart"""
    query = Cart.query.filter_by(status='active')
    if user_id:
        query = query.filter_by(user_id=user_id)
    else:
        query = query.filter_by(guest_token=guest_token)

    return Cart.query.first()
        
def get_all_carts():
    """get all cart"""
    return Cart.query.all()

def get_cart(cart_id):
    """get cart"""
    return Cart.query.get(cart_id)

def create_cart(data):
    """create cart"""
    cart_details_data = data.pop('cart_details',[])
    cart = Cart(**data)
    db.session.add(cart)
    db.session.flush()

    for items in cart_details_data:
        cart_detail = CartDetails(
            cart_id = cart.cart_id,
            menuitem_id = items['menuitem_id'],
            quantity = str(items['quantity'])
        )
        db.session.add(cart_detail)
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
