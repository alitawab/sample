"""schema for order"""

from marshmallow import Schema, fields, validates_schema, ValidationError

class OrderItemSchema(Schema):
    """function to validate order_item"""
    menuitem_id = fields.Int(required=True)
    quantity = fields.Int(required=True)
    unit_price = fields.Float(required=True)


class OrderSchema(Schema):
    """function to validata order"""
    order_id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    address_id = fields.Int(required=True)
    rider_id = fields.Int(required=False)
    resturant_id = fields.Int(required=True)
    total_price = fields.Float(required=True)
    stauts = fields.Str(required=True)
    created_at = fields.DateTime(required=True)
    items = fields.List(fields.Nested(OrderItemSchema),required=True)

@validates_schema
def validate_items(self, data, **kwargs):
    """function validata"""
    if not data.get("items"):
        raise ValidationError("At least one menu item is required")
