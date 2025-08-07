"""rider view module"""
from flask.views import MethodView
from flask import request, jsonify
from marshmallow import ValidationError

from app.schemas.rider_schema import RiderSchema
from app.services.rider_service import (
    get_all_riders, get_rider, get_rider_by_user_id, create_rider, update_rider, delete_rider
)

rider_schema = RiderSchema()
rider_list_schema = RiderSchema(many=True)

class RiderByUserApi(MethodView):
    """view model class"""
    def get(self, rider_id):
        """get rider by user id"""
        rider = get_rider_by_user_id(rider_id)
        if not rider:
            return jsonify({'error': 'Rider not found'}), 404
        return rider_schema.dump(rider), 200



class RiderAPI(MethodView):
    """view module class"""
    def get(self, rider_id=None):
        """Get all riders"""
        if rider_id:
            rider=get_rider(rider_id)
            if not rider:
                return jsonify({'error': 'Rider not found'}), 404
            return rider_schema.dump(rider),200
        riders = get_all_riders()
        return rider_schema.dump(riders) , 200

    def post(self):
        """Create a new rider"""
        data = request.get_json()
        try:
            valid_data = rider_schema.load(data)
        except ValidationError as err:
            return jsonify(err.messages), 400

        rider = create_rider(valid_data)
        return rider_schema.dump(rider),201

    def put (self, rider_id):
        """Update rider"""
        rider = get_rider(rider_id)
        if not rider:
            return jsonify({'error':'rider not found'}),404

        data = rider_schema.load(request.json(), partial=True)
        rider = update_rider(rider, data)
        return rider_schema.dump(rider),200

    def delete(self, rider_id):
        """delete rider"""
        rider = get_rider(rider_id)
        if not rider:
            return jsonify({'error':'rider not found'}), 404
        delete_rider(rider)
        return '', 204
