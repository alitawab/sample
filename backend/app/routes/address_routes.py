"""address routes"""
from flask import Blueprint, request, jsonify
from app.models import Address
from app.extensions import db

address_bp = Blueprint('address', __name__)

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
    new_address = Address (
        user_id = data['user_id'],
        street = data['street'],
        city = data['city'],
        state = data['state'],
        zip_code = data['zip_code'],
        longitude = data['longitude'],
        latitude = data['latitude'],
    )
    db.session.add(new_address)
    return jsonify({'message':'address created successfuly'}),201
