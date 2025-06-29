"""schema for users"""
from marshmallow import Schema, fields


class UsersSchema(Schema):
    """validate function for user"""
    user_id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True, load_only=True)
    phone = fields.Str(required=True)
