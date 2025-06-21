"""resturant routes"""
from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from app.models import Resturant
from app.extensions import db
from app.schemas.resturant_schema import ResturantSchema


resturant_bp = Blueprint('resturant', __name__)
resturant_schema = ResturantSchema()

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
    try:
        valid_data = resturant_schema.load(data)
    except ValidationError as err:
        return (err.messages), 400

    new_resturant = Resturant (
        name = valid_data['name'],
        address = valid_data['address'],
        logo_url = valid_data['logo_url'],
        phone = valid_data['phone'],
        rating = valid_data['rating'],
        open_hours = valid_data['open_hours'],
    )
    db.session.add(new_resturant)
    return jsonify({'message':'resturant created successfuly'}),201
