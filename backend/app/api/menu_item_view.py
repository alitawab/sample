from flask.views import MethodView
from flask import request, jsonify
from marshmallow import ValidationError
from app.models import MenuItem
from app.extensions import db
from app.schemas.menu_item_schema import MenuItemSchema

menuitem_schema = MenuItemSchema()
menuitem_list_schema = MenuItemSchema(many=True)

class MenuItemAPI(MethodView):
    def get(self):
        """Get all menu items"""
        menuitems = MenuItem.query.all()
        result = menuitem_list_schema.dump(menuitems)
        return jsonify(result), 200

    def post(self):
        """Create a new menu item"""
        data = request.get_json()
        try:
            valid_data = menuitem_schema.load(data)
        except ValidationError as err:
            return jsonify(err.messages), 400

        new_menuitem = MenuItem(
            resturant_id=valid_data['resturant_id'],
            name=valid_data['name'],
            description=valid_data['description'],
            price=valid_data['price'],
            image_url=valid_data['image_url'],
            is_available=valid_data['is_available']
        )

        db.session.add(new_menuitem)
        db.session.commit()

        return jsonify({'message': 'Menu item created successfully'}), 201
