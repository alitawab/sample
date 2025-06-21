"""cart schema"""
from marshmallow import Schema, fields

class CartSchema(Schema):
    """function to validate cart"""
    cart_id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    status = fields.Str(required=True)
