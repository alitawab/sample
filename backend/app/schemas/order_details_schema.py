"""schema order details"""
from marshmallow import Schema, fields

class OrderDetailsSchema(Schema):
    """functino to validate order details"""
    orderdetails_id = fields.Int(dump_only=True)
    oder_id = fields.Int(required=True)
    menuitem_id = fields.Int(required=True)
    quantity = fields.Int(required=True)
    unit_price = fields.Float(required=True)
