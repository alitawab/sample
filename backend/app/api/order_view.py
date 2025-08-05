"""class for order view"""
from flask.views import MethodView
from flask import request, jsonify
from marshmallow import ValidationError

from app.schemas.order_schema import OrderSchema
from app.services.order_service import (
    get_all_orders, get_order, get_order_by_status, create_order, update_order, delete_order
)

order_schema = OrderSchema()
order_list_schema = OrderSchema(many=True)

class OrderStatusApi(MethodView):
    """class for order status view"""
    def get(self):
        """get function"""
        pending_orders = get_order_by_status(status="Pending")
        return order_list_schema.dump(pending_orders), 200

    def put(self,order_id):
        """function to update status"""
        data = request.get_json()
        status = data.get("status")
        if not status:
            return jsonify({"error":"status not found"}),404
        order = get_order(order_id)
        if not order:
            return jsonify({"error":"Order not found"}),404

        update_order_status = update_order(order,{"status":status})
        return order_schema.dump(update_order_status),200


class OrderAPI(MethodView):
    """class for order view"""
    def get(self, order_id=None):
        """Get all orders or a specific order by ID"""
        if order_id:
            order = get_order(order_id)
            if not order:
                return jsonify ({'error':'order not found'}), 404
            return order_schema.dump(order), 200
        orders = get_all_orders()
        return order_list_schema.dump(orders), 200

    def post(self):
        """Create a new order"""
        data = request.get_json()

        try:
            valid_data = order_schema.load(data)
        except ValidationError as err:
            print(err.messages)
            return jsonify(err.messages), 400

        order = create_order(valid_data)
        return order_schema.dump(order), 201


    def put(self, order_id):
        """Update an order"""
        order = get_order(order_id)
        if not order:
            return jsonify({'error': 'order not found'}), 404
        data = order_schema.load(request.get_json(), partial= True)
        order = update_order(order, data)
        return order_schema.dump(order), 200


    def delete(self, order_id):
        """Delete an order"""
        order = get_order(order_id)
        if not order:
            return jsonify({'error': 'Order not found'}), 404

        delete_order(order)
        return '', 204
