"""cart schema"""
from marshmallow import Schema, fields


class CartDetailsSchema(Schema):
    """class for cart details schema"""
    cartdetails_id = fields.Int(dump_only=True)
    menuitem_id = fields.Int(required=True)
    quantity = fields.Int(required=True)

class CartSchema(Schema):
    """function to validate cart"""
    cart_id = fields.Int(dump_only=True)
    user_id = fields.Int(required=False, allow_none=True)
    guest_token = fields.Str(allow_none=True)
    cart_details = fields.List(fields.Nested(CartDetailsSchema),required=True)
    status = fields.Str(required=True)
