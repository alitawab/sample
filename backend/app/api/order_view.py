"""class for order view"""
from flask.views import MethodView
from flask import request, jsonify, abort
from app.models import Order
from app.extensions import db
# adjust according to your structure

class OrderAPI(MethodView):
    """class for order view"""
    def get(self, order_id=None):
        """Get all orders or a specific order by ID"""
        if order_id is None:
            orders = Order.query.all()
            return jsonify([{
                'order_id': o.order_id,
                'user_id': o.user_id,
                'address_id': o.address_id,
                'rider_id': o.rider_id,
                'resturant_id': o.resturant_id,
                'total_price': o.total_price,
                'status': o.status,
                'created_at': o.created_at,
            } for o in orders]), 200
        else:
            order = Order.query.get(order_id)
            if not order:
                abort(404, description="Order not found")
            return jsonify({
                'order_id': order.order_id,
                'user_id': order.user_id,
                'address_id': order.address_id,
                'rider_id': order.rider_id,
                'resturant_id': order.resturant_id,
                'total_price': order.total_price,
                'status': order.status,
                'created_at': order.created_at,
            }), 200

    def post(self):
        """Create a new order"""
        data = request.get_json()
        try:
            order = Order(
                user_id=data['user_id'],
                address_id=data['address_id'],
                rider_id=data.get('rider_id'),
                resturant_id=data['resturant_id'],
                total_price=data['total_price'],
                status=data.get('status', 'pending')
            )
            db.session.add(order)
            db.session.commit()
            return jsonify({'message': 'Order created', 'order_id': order.order_id}), 201
        except KeyError as e:
            abort(400, description=f"Missing field: {e.args[0]}")

    def put(self, order_id):
        """Update an order"""
        order = Order.query.get(order_id)
        if not order:
            abort(404, description="Order not found")

        data = request.get_json()
        order.user_id = data.get('user_id', order.user_id)
        order.address_id = data.get('address_id', order.address_id)
        order.rider_id = data.get('rider_id', order.rider_id)
        order.resturant_id = data.get('resturant_id', order.resturant_id)
        order.total_price = data.get('total_price', order.total_price)
        order.status = data.get('status', order.status)

        db.session.commit()
        return jsonify({'message': 'Order updated'}), 200

    def delete(self, order_id):
        """Delete an order"""
        order = Order.query.get(order_id)
        if not order:
            abort(404, description="Order not found")
        db.session.delete(order)
        db.session.commit()
        return jsonify({'message': 'Order deleted'}), 200
