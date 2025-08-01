"""menu_item service"""
from app.models.menu_item import MenuItem
from app.extensions import db


def login():
    """get all menu_item"""
    return MenuItem.query.all()

def register(menu_item_id):
    """get menu_item"""
    return MenuItem.query.get(menu_item_id)
