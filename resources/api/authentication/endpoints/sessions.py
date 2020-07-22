from flask_restplus import Resource

from resources import api
from resources.api.authentication import namespace
from resources.api.authentication.api_definition import session
from resources.api.authentication.domain_logic import (
    get_session,
    create_session,
    login,
    logout, get_session_by_token,
)
from resources.api.authentication.parsers import authentication_parser, login_parser


@namespace.route("/sessions")
class SessionResource(Resource):
    @api.expect(authentication_parser)
    @api.marshal_with(session)
    def get(self):
        args = authentication_parser.parse_args()
        return get_session_by_token(args["OpenAccessToken"])

    @api.expect(login_parser)
    @api.marshal_with(session)
    def post(self):
        args = login_parser.parse_args()
        return create_session(login(args["name"], args["password"]))

    @api.expect(authentication_parser)
    def delete(self):
        args = authentication_parser.parse_args()
        logout(get_session_by_token(args["OpenAccessToken"]))
        return {"status": "success"}
