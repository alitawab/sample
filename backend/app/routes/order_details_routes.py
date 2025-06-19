"""order details routes"""
from flask import Blueprint, request, jsonify
from app.models import OrderDetails
from app.extensions import db

order_details_bp = Blueprint('order_details', __name__)

@order_details_bp.route('/', methods=['GET'])

def get_orderdetails():
    """function get all order details"""
    orderdetails = OrderDetails.query.all()
    return jsonify([{
        'orderdetails_id':orderdetail.orderdetails_id,
        'order_id':orderdetail.order_id,
        'menuitem_id':orderdetail.menuitem_id,
        'quantity':orderdetail.quantity,
        'unit_price':orderdetail.unit_price,
    } for orderdetail in  orderdetails ]), 200

@order_details_bp.route('/',methods=['POST'])
def create_orderdetails():
    """function to create new orderdetails"""
    data = request.get_json()
    new_order_details = OrderDetails (
        order_id = data['order_id'],
        menu_item_id = data['menu_item_id'],
        quantity = data['quantity'],
        unit_price = data['unit_price']
    )
    db.session.add(new_order_details)
    return jsonify({'message':'orderdetails created successfuly'}),201
