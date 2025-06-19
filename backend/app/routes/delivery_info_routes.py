"""deliveryinfo routes"""
from flask import Blueprint, request, jsonify
from app.models import DeliveryInfo
from app.extensions import db

deliveryinfo_bp = Blueprint('deliveryinfo', __name__)

@deliveryinfo_bp.route('/', methods=['GET'])
def get_deliveryinfo():
    """function get all deliveryinfo"""
    deliveryinfos = DeliveryInfo.query.all()
    return jsonify([{
        'deliveryinfo_id':deliveryinfo.deliveryinfo_id,
        'rider_id':deliveryinfo.rider_id,
        'order_id':deliveryinfo.order_id,
        'pickup_time':deliveryinfo.pickup_time,
        'delivery_time':deliveryinfo.delivery_time,
        'status':deliveryinfo.status,

    } for deliveryinfo in  deliveryinfos ]), 200

deliveryinfo_bp.route('/',methods=['POST'])
def create_deliveryinfo():
    """function to create new deliveryinfo"""
    data = request.get_json()
    new_deliveryinfo = DeliveryInfo (
        rider_id = data['rider_id'],
        order_id = data['order_id'],
        pickup_time = data['pickup_time'],
        delivery_time = data['delivery_time'],
        status = data['status'],
    )
    db.session.add(new_deliveryinfo)
    return jsonify({'message':'deliveryinfo created successfuly'}),201
