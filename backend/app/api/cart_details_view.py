from flask.views import MethodView
from flask import request, jsonify, abort
from marshmallow import ValidationError
from app.models import CartDetails
from app.extensions import db
from app.schemas.cart_details_schema import CartDetailsSchema

cart_detail_schema = CartDetailsSchema()
cart_detail_list_schema = CartDetailsSchema(many=True)

class CartDetailsAPI(MethodView):
    def get(self):
        """Get all cart details"""
        cart_details = CartDetails.query.all()
        result = cart_detail_list_schema.dump(cart_details)
        return jsonify(result), 200

    def post(self):
        """Create new cart details"""
        data = request.get_json()
        try:
            valid_data = cart_detail_schema.load(data)
        except ValidationError as err:
            return jsonify(err.messages), 400

        new_cart_detail = CartDetails(
            cart_id=valid_data['cart_id'],
            menu_item_id=valid_data['menu_item_id'],
            quantity=valid_data['quantity']
        )
        db.session.add(new_cart_detail)
        db.session.commit()

        return jsonify({'message': 'Cart details created successfully'}), 201
