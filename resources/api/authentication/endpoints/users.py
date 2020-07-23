from flask_restplus import Resource

from resources.api import api
from resources.api.authentication import namespace
from resources.api.authentication.api_definition import user
from resources.api.authentication.domain_logic import get_session, change_password
from resources.api.authentication.parsers import authentication_parser, password_change_parser


@namespace.route("/users")
class UserResource(Resource):
    @api.expect(authentication_parser)
    @api.marshal_with(user)
    def get(self):
        args = authentication_parser.parse_args()
        return get_session(args["OpenAccessToken"])

    @api.expect(password_change_parser)
    def put(self):
        args = password_change_parser.parse_args()
        change_password(get_session(args["OpenAccessToken"]), args["current_password"], args["new_password"])
        return {"status": "success"}