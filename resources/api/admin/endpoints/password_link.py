from flask_restplus import Resource

from resources import api
from resources.api.admin import namespace
from resources.api.admin.domain_logic import check_admin
from resources.api.admin.parsers import user_target_parser
from resources.api.authentication.api_definition import password_link
from resources.api.authentication.domain_logic import (
    get_session,
    create_password_link,
    get_user_by_id,
    get_password_link_by_token,
    delete_password_link,
)
from resources.api.authentication.parsers import password_link_parser


@namespace.route("/password_link")
class AdminUsersResource(Resource):
    @api.marshal_with(password_link)
    @api.expect(user_target_parser)
    def post(self):
        args = user_target_parser.parse_args()
        check_admin(get_session(args["OpenAccessToken"]))
        return create_password_link(get_user_by_id(args["user_id"]))

    @api.expect(password_link_parser)
    def delete(self):
        args = password_link_parser.parse_args()
        check_admin(get_session(args["OpenAccessToken"]))
        delete_password_link(get_password_link_by_token(args["token"]))
        return {"status": "success"}
