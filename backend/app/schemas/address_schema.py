"""schema for address"""

from marshmallow import Schema, fields

class AddressSchema(Schema):
    """validate function for address"""

    address_id = fields.Int(dump_only=True)
    user_id = fields.Int(required=False, allow_none=True)
    street = fields.Str(required=True)
    city = fields.Str(required=True)
    state = fields.Str(required=True)
    zip_code = fields.Str(required=True)
    latitude = fields.Float(required=True)
    longitude = fields.Float(required=True)
