"""rider service"""
from app.models.rider import Rider
from app.extensions import db


def get_all_riders():
    """get all rider"""
    return Rider.query.all()

def get_rider(rider_id):
    """get rider"""
    return Rider.query.get(rider_id)

def create_rider(data):
    """create rider"""
    rider = Rider(**data)
    db.session.add(rider)
    db.session.commit()
    return rider

def update_rider(rider, data):
    """update rider"""
    for key, value in data.items():
        setattr(rider, key, value)
    db.session.commit()
    return rider

def delete_rider(rider):
    """delete rider"""
    db.session.delete(rider)
    db.session.commit()
