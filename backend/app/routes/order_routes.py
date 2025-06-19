"""order routes"""
from flask import Blueprint, request, jsonify
from app.models import Order
from app.extensions import db

order_bp = Blueprint('order', __name__)

@order_bp.route('/', methods=['GET'])
def get_order():
    """function get all order"""
    orders = Order.query.all()
    return jsonify([{
        'order_id':order.order_id,
        'user_id':order.user_id,
        'address_id':order.address_id,
        'rider_id':order.rider_id,
        'resturant_id':order.resturant_id,
        'total_price':order.total_price,
        'status':order.status,
        'created_at':order.created_at,


    } for order in  orders ]), 200

@order_bp.route('/',methods=['POST'])
def create_order():
    """function to create new order"""
    data = request.get_json()
    new_order = Order (
        user_id = data['user_id'],
        address_id = data['address_id'],
        rider_id = data['rider_id'],
        resturant_id = data['resturant_id'],
        total_price = data['total_price'],
        status = data['status'],
        created_at = data['created_at'],
    )
    db.session.add(new_order)
    return jsonify({'message':'order created successfuly'}),201
