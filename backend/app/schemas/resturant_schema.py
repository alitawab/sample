"""schema resturant"""
from marshmallow import Schema, fields
from app.schemas.menu_item_schema import MenuItemSchema

class ResturantSchema(Schema):
    """validate function for resturant schema"""
    resturant_id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    address = fields.Str(required=True)
    logo_url = fields.Str(required=True)
    phone = fields.Str(required=True)
    rating = fields.Float(required=True)
    tags = fields.Str(required=True)
    open_hours = fields.Str(required=True)

    menu_items = fields.Nested(MenuItemSchema, many=True, dump_only=True)
