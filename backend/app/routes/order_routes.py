"""order routes"""
from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.models import Order, OrderDetails
from app.extensions import db
from app.schemas.order_schema import OrderSchema

order_bp = Blueprint('order', __name__)
order_schema = OrderSchema()


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

    try:
        valid_data = order_schema.load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    new_order = Order (
        user_id = valid_data['user_id'],
        address_id = valid_data['address_id'],
        rider_id = valid_data['rider_id'],
        resturant_id = valid_data['resturant_id'],
        total_price = valid_data['total_price'],
        status = valid_data['status'],
        created_at = valid_data['created_at'],
        )
    db.session.add(new_order)
    db.session.flush()

    for item in data["items"]:
        order_item = OrderDetails(
        order_id=new_order.order_id,
        menuitem_id=item["menuitem_id"],
        quantity=item["quantity"],
        unit_price=item["unit_price"],
        )
        db.session.add(order_item)
    db.session.commit()
    return jsonify({'message':'Order created successfuly','order_id':new_order.order_id}),201


@order_bp.route('<int:user_id>',methods=['GET'])
def get_order_by_user(user_id):
    """get order by user function"""
    orders = Order.query.filter_by(user_id=user_id).all()

    result =[]
    for order in orders:
        order_dict = {
        'order_id':order.order_id,
        'resturant_id':order.resturant_id,
        'total_price':order.total_price,
        'status':order.status,
        'created_at':order.created_at,
        'items': []
        }

        for detail in order.order_details:
            order_dict ['items'].append({
                'menuitem_id':detail.menuitem_id,
                'quantity': detail.quantity,
                'unit_price':detail.unit_price
            })

        result.append(order_dict)

    return jsonify(result), 200
