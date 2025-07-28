from flask.views import MethodView
from flask import request, jsonify
from marshmallow import ValidationError
from app.services.menu_item_service import (
    get_all_menu_items, get_menu_item, create_menu_item, update_menu_item, delete_menu_item)

from app.schemas.menu_item_schema import MenuItemSchema

menuitem_schema = MenuItemSchema()
menuitem_list_schema = MenuItemSchema(many=True)

class MenuItemAPI(MethodView):
    """view module class"""
    def get(self, menu_item_id=None):
        """Get all users or a specific user by ID"""
        if menu_item_id:
            menu_item = get_menu_item(menu_item_id)
            if not menu_item:
                return jsonify({'error': 'Menu item not found'}), 404
            return menuitem_schema.dump(menu_item),200
        users = get_all_menu_items()
        return menuitem_schema.dump(users), 200

    def post(self):
        """Create a new menu item"""
        data = request.get_json()
        try:
            valid_data = menuitem_schema.load(data)
        except ValidationError as err:
            return jsonify(err.messages), 400

        user = create_menu_item(valid_data)
        return menuitem_schema.dump(user), 201

    def put(self, menu_item_id):
        """update menu item"""
        menu_item = get_menu_item(menu_item_id)
        if not menu_item:
            return jsonify({'error':'menu item not found'}), 404

        data = menuitem_schema.load(request.json(), partial=True)
        menu_item= update_menu_item(menu_item, data)
        return menuitem_schema.dump(menu_item), 200

    def delete(self, menu_item_id):
        """delete menu item"""
        menuitem = get_menu_item(menu_item_id)
        if not menuitem:
            return jsonify({'error': 'User not found'}), 404

        delete_menu_item(menuitem)
        return '', 204
