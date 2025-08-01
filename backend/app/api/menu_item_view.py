"""module for menu item view"""
import os
from flask.views import MethodView
from flask import request, jsonify
from werkzeug.utils import secure_filename
from marshmallow import ValidationError
from app.services.menu_item_service import (
    get_all_menu_items,
    get_menu_item,
    create_menu_item,
    update_menu_item,
    delete_menu_item,
    get_menu_item_by_resturant_id
    )

from app.schemas.menu_item_schema import MenuItemSchema

menuitem_schema = MenuItemSchema()
menuitem_list_schema = MenuItemSchema(many=True)

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'app', 'static', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

class MenuItemByResturantApi(MethodView):
    """Api view for get menu by resturant id """
    def get(self, resturant_id):
        """get menu item by resturant id"""
        menuitems = get_menu_item_by_resturant_id(resturant_id)
        return menuitem_list_schema.dump(menuitems or []), 200


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
        return menuitem_list_schema.dump(users), 200

    def post(self):
        """Create a new menu item"""
        data = request.form.to_dict()
        image = request.files.get('image')

        if image:
            filename = secure_filename(image.filename)
            image_path = os.path.join(UPLOAD_FOLDER,filename)
            image.save(image_path)
            image_url = f'/static/uploads/{filename}'
        else:
            image_url = ''

        data['image_url'] = image_url

        try:
            valid_data = menuitem_schema.load(data)
        except ValidationError as err:
            return jsonify(err.messages), 400

        menuitem = create_menu_item(valid_data)
        return menuitem_schema.dump(menuitem), 201

    def put(self, menu_item_id):
        """update menu item"""
        menu_item = get_menu_item(menu_item_id)
        if not menu_item:
            return jsonify({'error':'menu item not found'}), 404

        data = menuitem_schema.load(request.form, partial=True)
        if 'image' in request.files:
            image_file = request.files['image']
            if image_file and image_file.filename:
                if menu_item.image_url:
                    try:
                        file_name = os.path.basename(menu_item.image_url)
                        old_image_path = os.path.join(UPLOAD_FOLDER,file_name)
                        if os.path.exists(old_image_path):
                            os.remove(old_image_path)
                    except Exception as e:
                        print(f"Failed to Delete image:{e}")

                file_name = secure_filename(image_file.filename)
                image_path = os.path.join(UPLOAD_FOLDER,file_name)
                image_file.save(image_path)

                data['image_url'] = f"/static/uploads/{file_name}"

        update_menuitem= update_menu_item(menu_item, data)
        return menuitem_schema.dump(update_menuitem), 200

    def delete(self, menu_item_id):
        """delete menu item"""
        menuitem = get_menu_item(menu_item_id)
        if not menuitem:
            return jsonify({'error': 'User not found'}), 404

        if menuitem.image_url:
            try:
                file_name = os.path.basename(menuitem.image_url)
                old_image_path = os.path.join(UPLOAD_FOLDER,file_name)
                if os.path.exists(old_image_path):
                    os.remove(old_image_path)
            except Exception as e:
                print(f"Failed to Delete image:{e}")

        delete_menu_item(menuitem)
        return '', 204
