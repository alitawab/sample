"""rider schema"""
from marshmallow import Schema, fields

class RiderSchema(Schema):
    """function to validate rider schema"""
    rider_id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    name = fields.Str(required=True)
    phone = fields.Str(required=True)
    vehicle_type = fields.Str(required=True)
    current_location_lat = fields.Float(required=True)
    current_location_lng = fields.Float(required=True)
    license_number = fields.Str(required=True)
    is_available = fields.Boolean(required=True)
