"""resturant routes"""
from flask import Blueprint, request, jsonify
from app.models import Resturant
from app.extensions import db

resturant_bp = Blueprint('resturant', __name__)

@resturant_bp.route('/', methods=['GET'])
def get_resturant():
    """function get all resturant"""
    resturants = Resturant.query.all()
    return jsonify([{
        'id':resturant.resturant_id,
        'name':resturant.name,
        'address':resturant.address,
        'logo_url':resturant.logo_url,
        'phone':resturant.phone,
        'rating':resturant.rating,
        'open_hours':resturant.open_hours,

    } for resturant in  resturants ]), 200

@resturant_bp.route('/',methods=['POST'])
def create_resturant():
    """function to create new resturant"""
    data = request.get_json()
    new_resturant = Resturant (
        name = data['name'],
        address = data['address'],
        logo_url = data['logo_url'],
        phone = data['phone'],
        rating = data['rating'],
        open_hours = data['open_hours'],
    )
    db.session.add(new_resturant)
    return jsonify({'message':'resturant created successfuly'}),201
