"""cart view module"""
from flask.views import MethodView
from flask import request, jsonify
from marshmallow import ValidationError
from app.services.cart_service import (
    get_user_or_guest_cart, get_cart, create_cart, update_cart, delete_cart
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
        guest_token = request.args.get('guest_token')
        user_id = request.args.get('user_id')

        if not guest_token and not user_id:
            return jsonify({'error':'Missing guest_token and or user_id'}), 400

        if not cart:
            return jsonify({'error':'No cart found'}),404

        carts = get_user_or_guest_cart(user_id,guest_token)
        return cart_schema.dump(carts), 200

    def post(self):
        """Create a new cart"""
        data = request.get_json()
        print(data)
        try:
            valid_data = cart_schema.load(data)
        except ValidationError as err:
            return jsonify(err.messages), 400

        print("VALID",valid_data)
        cart = create_cart(valid_data)
        print("DATA SAVED", cart)

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
