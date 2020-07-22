from flask_restplus import Resource

from resources.api import api
from resources.api.authentication import namespace
from resources.api.authentication.domain_logic import (
    perform_password_link,
    get_password_link_by_token,
    get_session,
)
from resources.api.authentication.parsers import password_link_perform


@namespace.route("/password_link")
class PasswordLinkResource(Resource):
    @api.expect(password_link_perform)
    def put(self):
        args = password_link_perform.parse_args()
        user = get_session(args["OpenAccessToken"])
        perform_password_link(
            get_password_link_by_token(args["token"]), args["new_password"], user
        )
        return {"status": "success"}
