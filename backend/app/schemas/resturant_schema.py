"""schema resturant"""
from marshmallow import Schema, fields

class ResturantSchema(Schema):
    """validate function for resturant schema"""
    resturant_id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    address = fields.Str(required=True)
    logo_url = fields.Str(required=True)
    phone = fields.Str(required=True)
    rating = fields.Float(required=True)
    open_hours = fields.Str(required=True)
