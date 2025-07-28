"""address services"""
from app .models.address import Address
from app.extensions import db


def get_all_addresses():
    """get all addresses"""
    return Address.query.all()

def get_address(address_id):
    """get address"""
    return Address.query.get(address_id)

def create_address(data):
    """create address"""
    address= Address(**data)
    db.session.add(address)
    db.session.commit()
    return address

def update_address(address, data):
    """update address"""
    for key, value in data.item():
        setattr(address, key, value)
    db.session.commit()
    return address

def delete_address(address):
    """delete address"""
    db.session.delete(address)
    db.session.commit()
