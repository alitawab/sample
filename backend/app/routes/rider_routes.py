"""rider routes"""
from flask import Blueprint, request, jsonify
from app.models import Rider
from app.extensions import db
from app.schemas.rider_schema import RiderSchema
from marshmallow import ValidationError

rider_bp = Blueprint('rider', __name__)
rider_schema = RiderSchema()

@rider_bp.route('/', methods=['GET'])
def get_riders():
    """function get all riders"""
    riders = Rider.query.all()
    return jsonify([{
        'rider_id':rider.rider_id,
        'name':rider.name,
        'phone':rider.phone,
        'vehicle_type':rider.vehicle_type,
        'current_location_lat':rider.current_location_lat,
        'current_location_lng':rider.current_location_lng,
        'is_available':rider.is_available,

    } for rider in  riders ]), 200

@rider_bp.route('/',methods=['POST'])
def create_rider():
    """function to create new rider"""
    data = request.get_json()
    try:
        valid_data = rider_schema.load(data)
    except ValidationError as err:
        return jsonify(err.messages),400

    new_rider = Rider (
        name = valid_data['name'],
        phone = valid_data['phone'],
        vehicle_type = valid_data['vehicle_type'],
        current_location_lat = valid_data['current_location_lat'],
        current_location_lng = valid_data['current_location_lng'],
        is_available = valid_data['is_available'],
    )
    db.session.add(new_rider)
    return jsonify({'message':'rider created successfuly'}),201
