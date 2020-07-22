from flask_restplus import Resource

from resources.api import api
from resources.api.admin import namespace
from resources.api.admin.domain_logic import check_admin
from resources.api.admin.parsers import user_target_parser, user_creation_parser
from resources.api.authentication.api_definition import user
from resources.api.authentication.domain_logic import (
    get_session,
    get_user_by_id,
    create_user,
    delete_user,
)


@namespace.route("/users")
class AdminUsersResource(Resource):
    @api.marshal_with(user)
    @api.expect(user_target_parser)
    def get(self):
        args = user_target_parser.parse_args()
        check_admin(get_session(args["OpenAccessToken"]))
        return get_user_by_id(args["user_id"])

    @api.marshal_with(user)
    @api.expect(user_creation_parser)
    def post(self):
        args = user_creation_parser.parse_args()
        check_admin(get_session(args["OpenAccessToken"]))
        return create_user(args["name"], admin=args["admin"])

    @api.marshal_with(user)
    @api.expect(user_target_parser)
    def delete(self):
        args = user_target_parser.parse_args()
        check_admin(get_session(args["OpenAccessToken"]))

        delete_user(get_user_by_id(args["user_id"]))
