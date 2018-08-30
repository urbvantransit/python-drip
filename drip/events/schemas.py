# coding: utf8
from marshmallow import (Schema, fields)


class CreateEventSchema(Schema):

    email = fields.String()
    action = fields.String()
    prospect = fields.Boolean(default=True)
    properties = fields.Dict()
    occurred_at = fields.LocalDateTime()
