from marshmallow import Schema, fields


class UserSchema(Schema):
    """ Schema for parsing User arguments. """

    name = fields.Str()
