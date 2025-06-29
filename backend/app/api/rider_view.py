from flask.views import MethodView
from flask import request, jsonify
from marshmallow import ValidationError
from app.models import Rider
from app.extensions import db
from app.schemas.rider_schema import RiderSchema

rider_schema = RiderSchema()
rider_list_schema = RiderSchema(many=True)

class RiderAPI(MethodView):
    def get(self):
        """Get all riders"""
        riders = Rider.query.all()
        result = rider_list_schema.dump(riders)
        return jsonify(result), 200

    def post(self):
        """Create a new rider"""
        data = request.get_json()
        try:
            valid_data = rider_schema.load(data)
        except ValidationError as err:
            return jsonify(err.messages), 400

        new_rider = Rider(
            name=valid_data['name'],
            phone=valid_data['phone'],
            vehicle_type=valid_data['vehicle_type'],
            current_location_lat=valid_data['current_location_lat'],
            current_location_lng=valid_data['current_location_lng'],
            is_available=valid_data['is_available'],
        )

        db.session.add(new_rider)
        db.session.commit()

        return jsonify({'message': 'Rider created successfully'}), 201
