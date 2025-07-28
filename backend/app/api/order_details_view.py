"""module view order details"""
from flask.views import MethodView
from flask import request, jsonify
from marshmallow import ValidationError
from app.services.order_details_service import (
    get_all_order_details, get_order_details, create_order_details, update_order_details, delete_order_details
)
from app.schemas.order_details_schema import OrderDetailsSchema

order_detail_schema = OrderDetailsSchema()
order_detail_list_schema = OrderDetailsSchema(many=True)

class OrderDetailsAPI(MethodView):
    """class for order details"""
    def get(self, order_details_id=None):
        """Get all order details"""
        if order_details_id:
            user = get_order_details(order_details_id)
            if not user:
                return jsonify({'error': 'User not found'}), 404
            return order_detail_schema.dump(user),200
        users = get_all_order_details()
        return order_detail_schema.dump(users), 200


    def post(self):
        """Create new order details"""
        data = request.get_json()
        try:
            valid_data = order_detail_schema.load(data)
        except ValidationError as err:
            return jsonify(err.messages), 400

        user = create_order_details(valid_data)
        return order_detail_schema.dump(user), 201

    def put(self, order_details_id):
        """update user"""
        order_details = get_order_details(order_details_id)
        if not order_details:
            return jsonify({'error':'order_details not found'}), 404

        data = order_detail_schema.load(request.json(), partial=True)
        order_detail= update_order_details(order_details, data)
        return order_detail_schema.dump(order_detail), 200

    def delete(self, order_details_id):
        """delete user"""
        order_details = get_order_details(order_details_id)
        if not order_details:
            return jsonify({'error': 'User not found'}), 404

        delete_order_details(order_details)
        return '', 204
