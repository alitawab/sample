from flask.views import MethodView
from flask import request, jsonify
from marshmallow import ValidationError
from app.models import DeliveryInfo
from app.extensions import db
from app.schemas.delivery_info_schema import DeliveryInfoSchema

deliveryinfo_schema = DeliveryInfoSchema()
deliveryinfo_list_schema = DeliveryInfoSchema(many=True)

class DeliveryInfoAPI(MethodView):
    def get(self):
        """Get all delivery info records"""
        deliveryinfos = DeliveryInfo.query.all()
        result = deliveryinfo_list_schema.dump(deliveryinfos)
        return jsonify(result), 200

    def post(self):
        """Create a new delivery info record"""
        data = request.get_json()
        try:
            valid_data = deliveryinfo_schema.load(data)
        except ValidationError as err:
            return jsonify(err.messages), 400

        new_deliveryinfo = DeliveryInfo(
            rider_id=valid_data['rider_id'],
            order_id=valid_data['order_id'],
            pickup_time=valid_data['pickup_time'],
            delivery_time=valid_data['delivery_time'],
            status=valid_data['status'],
        )
        db.session.add(new_deliveryinfo)
        db.session.commit()

        return jsonify({'message': 'Delivery info created successfully'}), 201
