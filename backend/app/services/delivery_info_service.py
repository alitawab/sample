"""delivery_info service"""
from app.models.delivery_info import DeliveryInfo
from app.extensions import db


def get_all_delivery_infos():
    """get all delivery_info"""
    return DeliveryInfo.query.all()

def get_delivery_info(delivery_info_id):
    """get delivery_info"""
    return DeliveryInfo.query.get(delivery_info_id)

def create_delivery_info(data):
    """create delivery_info"""
    delivery_info = DeliveryInfo(**data)
    db.session.add(delivery_info)
    db.session.commit()
    return delivery_info

def update_delivery_info(delivery_info, data):
    """update delivery_info"""
    for key, value in data.items():
        setattr(delivery_info, key, value)
    db.session.commit()
    return delivery_info

def delete_delivery_info(delivery_info):
    """delete delivery_info"""
    db.session.delete(delivery_info)
    db.session.commit()
