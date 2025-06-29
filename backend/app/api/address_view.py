"""address view module"""
from flask.views import MethodView
from flask import request, jsonify
from marshmallow import ValidationError
from app.models import Address
from app.extensions import db
from app.schemas.address_schema import AddressSchema

address_schema = AddressSchema()
address_list_schema = AddressSchema(many=True)

class AddressAPI(MethodView):
    """api endpoint for address"""
    def get(self):
        """Get all addresses"""
        addresses = Address.query.all()
        result = address_list_schema.dump(addresses)
        return jsonify(result), 200

    def post(self):
        """Create a new address"""
        data = request.get_json()
        try:
            valid_data = address_schema.load(data)
        except ValidationError as err:
            return jsonify(err.messages), 400

        new_address = Address(
            user_id=valid_data['user_id'],
            street=valid_data['street'],
            city=valid_data['city'],
            state=valid_data['state'],
            zip_code=valid_data['zip_code'],
            longitude=valid_data['longitude'],
            latitude=valid_data['latitude'],
        )
        db.session.add(new_address)
        db.session.commit()

        return jsonify({'message': 'Address created successfully'}), 201
