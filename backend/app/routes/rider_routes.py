"""rider routes"""
from flask import Blueprint, request, jsonify
from app.models import Rider
from app.extensions import db

rider_bp = Blueprint('rider', __name__)

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
    new_rider = Rider (
        name = data['name'],
        phone = data['phone'],
        vehicle_type = data['vehicle_type'],
        current_location_lat = data['current_location_lat'],
        current_location_lng = data['current_location_lng'],
        is_available = data['is_available'],
    )
    db.session.add(new_rider)
    return jsonify({'message':'rider created successfuly'}),201
