"""resturant service"""
from app.models.resturant import Resturant
from app.extensions import db


def get_all_resturants():
    """get all resturant"""
    return Resturant.query.all()

def get_resturant(resturant_id):
    """get resturant"""
    return Resturant.query.get(resturant_id)

def get_resturant_by_user_id(user_id):
    """get resturant by user id """
    return Resturant.query.filter_by(user_id=user_id).first()

def create_resturant(data):
    """create resturant"""
    resturant = Resturant(**data)
    db.session.add(resturant)
    db.session.commit()
    return resturant

def update_resturant(resturant, data):
    """update resturant"""
    for key, value in data.items():
        setattr(resturant, key, value)
    db.session.commit()
    return resturant

def delete_resturant(resturant):
    """delete resturant"""
    db.session.delete(resturant)
    db.session.commit()
