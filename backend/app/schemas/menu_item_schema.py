"""menu item schema"""
from marshmallow import Schema, fields

class MenuItemSchema(Schema):
    """function to validate menu item"""
    menuitem_id = fields.Int(dump_only=True)
    resturant_id = fields.Int(required=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    price = fields.Float(required=True)
    image_url = fields.Str(required=True)
    is_available = fields.Boolean(required=True)
