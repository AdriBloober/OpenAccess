from flask_restplus import fields

from resources.api import api
from resources.api.authentication.api_definition import user

custom_header = api.model(
    "Custom Header",
    {
        "id": fields.Integer(readOnly=True),
        "header_name": fields.String(required=True),
        "header_content": fields.String(required=False, default=None),
    },
)

site = api.model(
    "Site",
    {
        "id": fields.Integer(readOnly=True),
        "name": fields.String(required=True),
        "host": fields.String(required=True),
        "proxy_pass_url": fields.String(required=True),
    },
)
custom_header_with_site = api.inherit(
    "Custom header with site", custom_header, {"site": fields.Nested(site)}
)
site_with_headers = api.inherit(
    "Site with headers",
    site,
    {"custom_headers": fields.List(fields.Nested(custom_header))},
)

site_with_users = api.inherit(
    "Site with users", site_with_headers, {"users": fields.List(fields.Nested(user))}
)

user_with_sites = api.inherit(
    "User with sites", user, {"sites": fields.List(fields.Nested(site))}
)
