from flask_restplus import fields

from resources import api

# TODO : stites list
user = api.model(
    "User",
    {
        "id": fields.Integer(readOnly=True),
        "name": fields.String(required=True),
        "admin": fields.Boolean(required=True, default=False),
    },
)

session = api.model(
    "Session",
    {
        "id": fields.Integer(readOnly=True),
        "token": fields.String(required=True),
        "user": fields.Nested(user),
    },
)
