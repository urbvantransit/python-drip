# coding: utf8
from marshmallow import (Schema, fields)


class TagSchema(Schema):

    email = fields.String()
    tag = fields.String()
