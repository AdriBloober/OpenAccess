from flask_restplus import Resource

from resources.api import api
from resources.api.authentication import namespace
from resources.api.authentication.api_definition import user
from resources.api.authentication.domain_logic import get_session
from resources.api.authentication.parsers import authentication_parser


@namespace.route("/users")
class UserResource(Resource):
    @api.expect(authentication_parser)
    @api.marshal_with(user)
    def get(self):
        args = authentication_parser.parse_args()
        return get_session(args["OpenAccessToken"])
