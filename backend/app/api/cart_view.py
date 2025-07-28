"""cart view module"""
from flask.views import MethodView
from flask import request, jsonify
from marshmallow import ValidationError
from app.services.cart_service import (
    get_all_carts, get_cart, create_cart, update_cart, delete_cart
)
from app.schemas.cart_schema import CartSchema


cart_schema = CartSchema()
cart_list_schema = CartSchema(many=True)

class CartAPI(MethodView):
    """view module class"""
    def get(self, cart_id=None):
        """Get all users or a specific user by ID"""
        if cart_id:
            cart = get_cart(cart_id)
            if not cart:
                return jsonify({'error': 'Cart not found'}), 404
            return cart_schema.dump(cart),200
        carts = get_all_carts()
        return cart_schema.dump(carts), 200

    def post(self):
        """Create a new cart"""
        data = request.get_json()
        try:
            valid_data = cart_schema.load(data)
        except ValidationError as err:
            return jsonify(err.messages), 400

        cart = create_cart(valid_data)
        return cart_schema.dump(cart), 201

    def put(self, cart_id):
        """update cart"""
        cart = get_cart(cart_id)
        if not cart:
            return jsonify({'error':'cart not found'}), 404

        data = cart_schema.load(request.json(), partial=True)
        cart= update_cart(cart, data)
        return cart_schema.dump(cart), 200

    def delete(self, cart_id):
        """delete cart"""
        cart = get_cart(cart_id)
        if not cart:
            return jsonify({'error': 'cart not found'}), 404

        delete_cart(cart)
        return '', 204
