"""menuitem routes"""
from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.models import MenuItem
from app.extensions import db
from app.schemas.menu_item_schema import MenuItemSchema

menuitem_bp = Blueprint('menu_item', __name__)
menuitem_schema = MenuItemSchema()

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

    try:
        valid_data = menuitem_schema.load(data)
    except ValidationError as err:
        return (err.messages),4000

    new_menuitem = MenuItem (
        resturant_id = valid_data['resturant_id'],
        name = valid_data['name'],
        description = valid_data['description'],
        price = valid_data['price'],
        image_url = valid_data['image_url'],
        is_available = valid_data['is_available'],

    )
    db.session.add(new_menuitem)
    return jsonify({'message':'menuitem created successfuly'}),201
