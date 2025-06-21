"""address routes"""
from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.models import Address
from app.extensions import db
from app.schemas.address_schema import AddressSchema

address_bp = Blueprint('address', __name__)
address_schema = AddressSchema()

@address_bp.route('/', methods=['GET'])
def get_address():
    """function get all address"""
    addresses = Address.query.all()
    return jsonify([{
        'address_id':address.address_id,
        'user_id':address.user_id,
        'street':address.street,
        'city':address.city,
        'state':address.state,
        'zip_code':address.zip_code,
        'latitude':address.latitude,
        'longitude':address.longitude
    } for address in addresses ]), 200

@address_bp.route('/',methods=['POST'])
def create_address():
    """function to create new address"""
    data = request.get_json()
    try:
        valid_data = address_schema.load(data)
    except ValidationError as err:
        return (err.messages),400

    new_address = Address (
        user_id = valid_data['user_id'],
        street = valid_data['street'],
        city = valid_data['city'],
        state = valid_data['state'],
        zip_code = valid_data['zip_code'],
        longitude = valid_data['longitude'],
        latitude = valid_data['latitude'],
    )
    db.session.add(new_address)
    return jsonify({'message':'address created successfuly'}),201
