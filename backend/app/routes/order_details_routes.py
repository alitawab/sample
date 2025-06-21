"""order details routes"""
from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.schemas.order_details_schema import OrderDetailsSchema
from app.models import OrderDetails
from app.extensions import db

order_details_bp = Blueprint('order_details', __name__)
order_detail_schema = OrderDetailsSchema()

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
    try:
        valid_data = order_detail_schema.load(data)
    except ValidationError as err:
        return (err.messages),400

    new_order_details = OrderDetails (
        order_id = valid_data['order_id'],
        menu_item_id = valid_data['menu_item_id'],
        quantity = valid_data['quantity'],
        unit_price = valid_data['unit_price']
    )
    db.session.add(new_order_details)
    return jsonify({'message':'orderdetails created successfuly'}),201
