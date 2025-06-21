"""schema cart details"""
from marshmallow import Schema, fields

class CartDetailsSchema(Schema):
    """function to validate cart details"""
    cartdetails_id = fields.Int(dump_only=True)
    cart_id = fields.Int(required=True)
    menuitem_id = fields.Int(required=True)
    quantity = fields.Str(required=True)
