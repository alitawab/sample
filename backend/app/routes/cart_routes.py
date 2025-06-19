"""cart routes"""
from flask import Blueprint, request, jsonify
from app.models import Cart
from app.extensions import db

cart_bp = Blueprint('cart', __name__)

@cart_bp.route('/', methods=['GET'])
def get_carts():
    """function get all cart"""
    carts = Cart.query.all()
    return jsonify([{
        'cart_id':cart.cart_id,
        'user_id':cart.user_id,
        'status':cart.status,
    } for cart in  carts ]), 200

@cart_bp.route('/',methods=['POST'])
def create_cart():
    """function to create new cart"""
    data = request.get_json()
    new_cart = Cart (
        user_id = data['user_id'],
        status = data['status'],
    )
    db.session.add(new_cart)
    return jsonify({'message':'cart created successfuly'}),201
