"""delivery info schema"""
from marshmallow import Schema, fields

class DeliveryInfoSchema(Schema):
    """functino to validate delivery info"""
    deliveryinfo_id = fields.Int(dump_only=True)
    rider_id = fields.Int(required=True)
    order_id = fields.Int(required=True)
    pickup_time = fields.DateTime(required=True)
    delivery_time = fields.DateTime(required=True)
    status = fields.Str(required=True)
