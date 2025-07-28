"""address view module"""
from flask.views import MethodView
from flask import request, jsonify
from marshmallow import ValidationError
from app.schemas.address_schema import AddressSchema
from app.services.address_service import (
    get_all_addresses, get_address, create_address, update_address, delete_address
)
address_schema = AddressSchema()
address_list_schema = AddressSchema(many=True)

class AddressAPI(MethodView):
    
    """view module class"""
    def get(self, address_id=None):
        """Get all  or a specific user by ID"""
        if address_id:
            address = get_address(address_id)
            if not address:
                return jsonify({'error': 'adddress not found'}), 404
            return address_schema.dump(address),200
        addresses = get_all_addresses()
        return address_schema.dump(addresses), 200

    def post(self):
        """Create a new address"""
        data = request.get_json()
        try:
            valid_data = address_schema.load(data)
        except ValidationError as err:
            return jsonify(err.messages), 400

        address = create_address(valid_data)
        return address_schema.dump(address), 201

    def put(self, address_id):
        """update address"""
        address = get_address(address_id)
        if not address:
            return jsonify({'error':'address not found'}), 404

        data = address_schema.load(request.json(), partial=True)
        address= update_address(address, data)
        return address_schema.dump(address), 200

    def delete(self, address_id):
        """delete address"""
        address = get_address(address_id)
        if not address:
            return jsonify({'error': 'address not found'}), 404

        delete_address(address)
        return '', 204
