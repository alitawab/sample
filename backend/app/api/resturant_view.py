"""resturant view module"""
import os
from flask.views import MethodView
from flask import request, jsonify
from marshmallow import ValidationError
from werkzeug.utils import secure_filename

from app.schemas.resturant_schema import ResturantSchema
from app.services.resturant_service import (
    get_all_resturants, get_resturant, create_resturant, update_resturant, delete_resturant, get_resturant_by_user_id
)

resturant_schema = ResturantSchema()
resturant_list_schema = ResturantSchema(many=True)
UPLOAD_FOLDER = 'static/uploads'

class ResturantByUserApi(MethodView):
    def get(self, user_id):
        resturant = get_resturant_by_user_id(user_id)
        if not resturant:
            return jsonify({'error': 'Restaurant not found'}), 404
        return resturant_schema.dump(resturant), 200


class ResturantAPI(MethodView):
    """view module resturant"""
    def get(self, resturant_id=None):
        """Get all restaurants"""
        user_id = request.args.get('user_id')
        print (user_id)
        if resturant_id:
            resturant = get_resturant(resturant_id)
            if not resturant:
                return jsonify({'error': 'Resturant not found'}), 404
            return resturant_schema.dump(resturant), 200

        if user_id:
            resturant = get_resturant_by_user_id(user_id)
            if not resturant:
                return jsonify({'error':'Resturant not found'}), 404
            return resturant_schema.dump(resturant), 200

        resturants = get_all_resturants()
        return resturant_list_schema.dump(resturants),200

    def post(self):
        """Create a new restaurant"""
        data = request.get_json()
        image = request.files.get('image')

        if image:
            filename = secure_filename(image.filename)
            image_path = os.path.join(UPLOAD_FOLDER, filename)
            image.save(image_path)
            image_url = f'/static/uploads/{filename}'
        else:
            image_url = ''


        data['logo_url'] = image_url
        try:
            valid_data = resturant_schema.load(data)
        except ValidationError as err:
            return jsonify(err.messages), 400
        resturant = create_resturant(valid_data)
        return resturant_schema.dump(resturant), 201

    def put(self, resturant_id):
        """Update restaurant"""
        resturant = get_resturant(resturant_id)
        if not resturant:
            return jsonify({'error': 'Resturant not found'}), 404

        data = resturant_schema.load(request.json(), partial=True)
        resturant = update_resturant(resturant, data)
        return resturant_schema.dump(resturant), 200

    def delete(self, resturant_id):
        """Delete restaurant"""
        resturant = get_resturant(resturant_id)
        if not resturant:
            return jsonify({'error': 'Resturant not found'}), 404

        delete_resturant(resturant)
        return '', 204
