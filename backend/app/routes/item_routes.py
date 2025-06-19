from flask import Blueprint, request, jsonify
from app.extensions import db
from backend.app.models.address import Item


item_bp = Blueprint('item_bp', __name__)

@item_bp.route('/item', methods=['GET'])
def get_items():
    items = Item.query.all()
    response = []

    for item in items:
        data = item.to_dict()
        jsonify(data)
        response.append(data)

    return (response,200)


@item_bp.route('/item', methods=['POST'])
def create_item():
    data = request.get_json()
    item = Item(name=data['name'])
    db.session.add(item)
    db.session.commit()
    return jsonify(item.to_dict()), 201
