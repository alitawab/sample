"""menu_item service"""
from app.models.menu_item import MenuItem
from app.extensions import db


def get_all_menu_items():
    """get all menu_item"""
    return MenuItem.query.all()

def get_menu_item(menu_item_id):
    """get menu_item"""
    return MenuItem.query.get(menu_item_id)

def create_menu_item(data):
    """create menu_item"""
    menu_item = MenuItem(**data)
    db.session.add(menu_item)
    db.session.commit()
    return menu_item

def update_menu_item(menu_item, data):
    """update menu_item"""
    for key, value in data.items():
        setattr(menu_item, key, value)
    db.session.commit()
    return menu_item

def delete_menu_item(menu_item):
    """delete menu_item"""
    db.session.delete(menu_item)
    db.session.commit()
