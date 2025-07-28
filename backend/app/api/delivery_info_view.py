from flask.views import MethodView
from flask import request, jsonify
from marshmallow import ValidationError
from app.services.delivery_info_service import (
    get_all_delivery_infos, get_delivery_info, create_delivery_info, update_delivery_info, delete_delivery_info
)
from app.schemas.delivery_info_schema import DeliveryInfoSchema

deliveryinfo_schema = DeliveryInfoSchema()
deliveryinfo_list_schema = DeliveryInfoSchema(many=True)

class DeliveryInfoAPI(MethodView):
    """view module class"""
    def get(self, deliveryinfo_id=None):
        """Get all users or a specific user by ID"""
        if deliveryinfo_id:
            deliveryinfo = get_delivery_info(deliveryinfo_id)
            if not deliveryinfo:
                return jsonify({'error': 'delivery info not found'}), 404
            return deliveryinfo_schema.dump(deliveryinfo),200
        deliveryinfos = get_all_delivery_infos()
        return deliveryinfo_schema.dump(deliveryinfos), 200

    def post(self):
        """Create a new delivery info"""
        data = request.get_json()
        try:
            valid_data = deliveryinfo_schema.load(data)
        except ValidationError as err:
            return jsonify(err.messages), 400

        deliveryinfo = create_delivery_info(valid_data)
        return deliveryinfo_schema.dump(deliveryinfo), 201

    def put(self, deliveryinfo_id):
        """update deilvery info"""
        deliveryinfo = get_delivery_info(deliveryinfo_id)
        if not deliveryinfo:
            return jsonify({'error':'delivery info not found'}), 404

        data = deliveryinfo_schema.load(request.json(), partial=True)
        deliveryinfo= update_delivery_info(deliveryinfo, data)
        return deliveryinfo_schema.dump(deliveryinfo), 200

    def delete(self, deliveryinfo_id):
        """delete delivery info"""
        deliveryinfo = get_delivery_info(deliveryinfo_id)
        if not deliveryinfo:
            return jsonify({'error': 'delivery info not found'}), 404

        delete_delivery_info(deliveryinfo)
        return '', 204
