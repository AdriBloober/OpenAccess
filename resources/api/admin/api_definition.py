from flask_restplus import fields

from resources.api import api
from resources.api.authentication.api_definition import user

site = api.model(
    "Site",
    {
        "id": fields.Integer(readOnly=True),
        "name": fields.String(required=True),
        "host": fields.String(required=True),
        "proxy_pass_url": fields.String(required=True),
    },
)

site_with_users = api.inherit(
    "Site with users", site, {"users": fields.List(fields.Nested(user))}
)

user_with_sites = api.inherit(
    "User with sites", user, {"sites": fields.List(fields.Nested(site))}
)
