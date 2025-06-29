from flask.views import MethodView
from flask import request, jsonify
from marshmallow import ValidationError
from app.models import Resturant
from app.extensions import db
from app.schemas.resturant_schema import ResturantSchema

resturant_schema = ResturantSchema()
resturant_list_schema = ResturantSchema(many=True)

class ResturantAPI(MethodView):
    def get(self):
        """Get all restaurants"""
        resturants = Resturant.query.all()
        result = resturant_list_schema.dump(resturants)
        return jsonify(result), 200

    def post(self):
        """Create a new restaurant"""
        data = request.get_json()
        try:
            valid_data = resturant_schema.load(data)
        except ValidationError as err:
            return jsonify(err.messages), 400

        new_resturant = Resturant(
            name=valid_data['name'],
            address=valid_data['address'],
            logo_url=valid_data['logo_url'],
            phone=valid_data['phone'],
            rating=valid_data['rating'],
            open_hours=valid_data['open_hours'],
        )

        db.session.add(new_resturant)
        db.session.commit()

        return jsonify({'message': 'Restaurant created successfully'}), 201
