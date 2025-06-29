from flask.views import MethodView
from flask import request, jsonify
from marshmallow import ValidationError
from app.schemas.order_details_schema import OrderDetailsSchema
from app.models import OrderDetails
from app.extensions import db

order_detail_schema = OrderDetailsSchema()
order_detail_list_schema = OrderDetailsSchema(many=True)

class OrderDetailsAPI(MethodView):
    def get(self):
        """Get all order details"""
        orderdetails = OrderDetails.query.all()
        result = order_detail_list_schema.dump(orderdetails)
        return jsonify(result), 200

    def post(self):
        """Create new order details"""
        data = request.get_json()
        try:
            valid_data = order_detail_schema.load(data)
        except ValidationError as err:
            return jsonify(err.messages), 400

        new_order_detail = OrderDetails(
            order_id=valid_data['order_id'],
            menu_item_id=valid_data['menu_item_id'],
            quantity=valid_data['quantity'],
            unit_price=valid_data['unit_price']
        )
        db.session.add(new_order_detail)
        db.session.commit()

        return jsonify({'message': 'Order details created successfully'}), 201
