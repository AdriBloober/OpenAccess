from flask_restplus import inputs

from resources.api.authentication.parsers import authentication_parser

user_target_parser = authentication_parser.copy()
user_target_parser.add_argument("user_id", type=int, required=True, help="The id of the targeted user.")

user_creation_parser = authentication_parser.copy()
user_creation_parser.add_argument("name", type=str, required=True, help="The name of the user.")
user_creation_parser.add_argument("admin", type=inputs.boolean, required=True, default=False, help="The name of the user.")