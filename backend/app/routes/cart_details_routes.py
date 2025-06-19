"""cartdetails routes"""
from flask import Blueprint, request, jsonify
from app.models import CartDetails
from app.extensions import db

cart_details_bp = Blueprint('cart_details', __name__)

@cart_details_bp.route('/', methods=['GET'])
def get_cartdetails():
    """function get all address"""
    cartdetails = CartDetails.query.all()
    return jsonify([{
        'cartdetails_id':cartdetail.cartdetails_id,
        'cart_id':cartdetail.cart_id,
        'menuitem_id':cartdetail.menuitem_id,
        'quantity':cartdetail.quantity,
    } for cartdetail in  cartdetails ]), 200

@cart_details_bp.route('/',methods=['POST'])
def create_cartdetails():
    """function to create new cartdetails"""
    data = request.get_json()
    new_cart_details = CartDetails (
        cart_id = data['cart_id'],
        menu_item_id = data['menu_item_id'],
        quantity = data['quantity']
    )
    db.session.add(new_cart_details)
    return jsonify({'message':'cartdetails created successfuly'}),201
