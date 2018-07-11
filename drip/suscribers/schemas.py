# coding: utf8
from marshmallow import (Schema, fields)


class CreateSuscriberSchema(Schema):

    email = fields.String()
    new_email = fields.String()
    user_id = fields.String()
    time_zone = fields.String()
    lifetime_value = fields.Integer()
    ip_address = fields.String()
    custom_fields = fields.Dict()
    tags = fields.List(fields.String())
    remove_tags = fields.List(fields.String())
    prospect = fields.Boolean()
    base_lead_score = fields.Integer()
    eu_consent = fields.String()
    eu_consent_message = fields.String()
