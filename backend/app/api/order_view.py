"""class for order view"""
from flask.views import MethodView
from flask import request, jsonify
from marshmallow import ValidationError

from app.schemas.order_schema import OrderSchema
from app.services.order_service import (
    get_all_orders, get_order, get_order_by_resturant, get_order_by_rider, get_order_by_status, create_order, update_order, delete_order
)
from app.services.rider_service import get_rider,update_rider

order_schema = OrderSchema()
order_list_schema = OrderSchema(many=True)

class OrderResturantApi(MethodView):
    """class for order status view"""
    def get(self):
        """get function"""
        resturant_id = request.args.get("resturant_id",type=int)

        orders = get_order_by_resturant(resturant_id)
        return order_list_schema.dump(orders), 200

class OrderStatusApi(MethodView):
    """class for order status view"""
    def get(self):
        """get function"""
        statuses = request.args.getlist("status")
        rider_id = request.args.get("rider_id",type=int)

        if not statuses:
            return jsonify({"error":"Status query error"}),400

        pending_orders = get_order_by_status(statuses,rider_id)
        return order_list_schema.dump(pending_orders), 200


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
        json_data = request.get_json()

        if not order:
            return jsonify({'error': 'order not found'}), 404

        payload = json_data.get("payload", {}) if json_data else {}
        allowed_keys = {'status','rider_id'}
        data = {k: v for k, v in payload.items() if k in allowed_keys}

        valid_data = order_schema.load(data, partial=True)

        if "rider_id" in valid_data:
            rider = get_rider(valid_data["rider_id"])
            if rider:
                update_rider(rider, {"is_available":False})


        if valid_data.get("status") == "Delivered" and order.rider_id:
            rider = get_rider(order.rider_id)
            if rider:
                update_rider(rider, {"is_available":True})


        order = update_order(order, valid_data)
        return order_schema.dump(order), 200


    def delete(self, order_id):
        """Delete an order"""
        order = get_order(order_id)
        if not order:
            return jsonify({'error': 'Order not found'}), 404

        delete_order(order)
        return '', 204
