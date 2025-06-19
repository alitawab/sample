"""menuitem routes"""
from flask import Blueprint, request, jsonify
from app.models import MenuItem
from app.extensions import db

menuitem_bp = Blueprint('menu_item', __name__)

@menuitem_bp.route('/', methods=['GET'])
def get_cartdetails():
    """function get all menuitems"""
    menuitems = MenuItem.query.all()
    return jsonify([{
        'menuitem_id':menuitem.menuitem_id,
        'resturant_id':menuitem.resturant_id,
        'name':menuitem.name,
        'description':menuitem.description,
        'price':menuitem.price,
        'image_url':menuitem.image_url,
        'is_available':menuitem.is_available,

    } for menuitem in  menuitems ]), 200

@menuitem_bp.route('/',methods=['POST'])
def create_menuitem():
    """function to create new menuitem"""
    data = request.get_json()
    new_menuitem = MenuItem (
        resturant_id = data['resturant_id'],
        name = data['name'],
        description = data['description'],
        price = data['price'],
        image_url = data['image_url'],
        is_available = data['is_available'],

    )
    db.session.add(new_menuitem)
    return jsonify({'message':'menuitem created successfuly'}),201
