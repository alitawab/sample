"""cart module view"""
from flask.views import MethodView
from flask import request, jsonify
from marshmallow import ValidationError
from app.schemas.cart_details_schema import CartDetailsSchema
from app.services.cart_details_service import (
    get_all_cart_details, get_cart_detail, create_cart_detail, update_cart_detail, delete_cart_detail
)

cart_detail_schema = CartDetailsSchema()
cart_detail_list_schema = CartDetailsSchema(many=True)

class CartDetailsAPI(MethodView):
    """view module class"""
    def get(self, cartdetails_id=None):
        """Get all users or a specific user by ID"""
        if cartdetails_id:
            cartdetails = get_cart_detail(cartdetails_id)
            if not cartdetails:
                return jsonify({'error': 'User not found'}), 404
            return cart_detail_schema.dump(cartdetails),200
        cartdetails = get_all_cart_details()
        return cart_detail_schema.dump(cartdetails), 200

    def post(self):
        """Create a new cart details"""
        data = request.get_json()
        try:
            valid_data = cart_detail_schema.load(data)
        except ValidationError as err:
            return jsonify(err.messages), 400

        cartdetails = create_cart_detail(valid_data)
        return cart_detail_schema.dump(cartdetails), 201

    def put(self, cartdetails_id):
        """update cart details"""
        cartdetails = get_cart_detail(cartdetails_id)
        if not cartdetails:
            return jsonify({'error':'user not found'}), 404

        data = cart_detail_schema.load(request.json(), partial=True)
        cartdetails= update_cart_detail(cartdetails, data)
        return cart_detail_schema.dump(cartdetails), 200

    def delete(self, cartdetails_id):
        """delete cart details"""
        cartdetails = get_cart_detail(cartdetails_id)
        if not cartdetails:
            return jsonify({'error': 'cart details not found'}), 404

        delete_cart_detail(cartdetails)
        return '', 204
