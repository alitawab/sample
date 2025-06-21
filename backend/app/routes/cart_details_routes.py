"""cartdetails routes"""
from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.models import CartDetails
from app.extensions import db
from app.schemas.cart_details_schema import CartDetailsSchema

cart_details_bp = Blueprint('cart_details', __name__)
cart_detail_schema = CartDetailsSchema()


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
    try:
        valid_data = cart_detail_schema.load(data)
    except ValidationError as err:
        return (err.messages),400

    new_cart_details = CartDetails (
        cart_id = valid_data['cart_id'],
        menu_item_id = valid_data['menu_item_id'],
        quantity = valid_data['quantity']
    )
    db.session.add(new_cart_details)
    return jsonify({'message':'cartdetails created successfuly'}),201
