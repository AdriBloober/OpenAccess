from flask_restplus import inputs

from resources.api.authentication.parsers import authentication_parser

user_target_parser = authentication_parser.copy()
user_target_parser.add_argument(
    "user_id", type=int, required=True, help="The id of the targeted user."
)

user_creation_parser = authentication_parser.copy()
user_creation_parser.add_argument(
    "name", type=str, required=True, help="The name of the user."
)
user_creation_parser.add_argument(
    "admin",
    type=inputs.boolean,
    required=True,
    default=False,
    help="The name of the user.",
)

site_creation_parser = authentication_parser.copy()
site_creation_parser.add_argument("name", type=str, required=True)
site_creation_parser.add_argument(
    "host", type=str, required=True, help="The hostname for this site/domain."
)
site_creation_parser.add_argument(
    "proxy_pass_url",
    type=str,
    required=True,
    help="The server will send the requst to this url.",
)

site_target_parser = authentication_parser.copy()
site_target_parser.add_argument("site_id", type=int, required=True)

site_changing_parser = site_target_parser.copy()
site_changing_parser.add_argument(
    "host", type=str, required=False, help="The hostname for this site/domain."
)
site_changing_parser.add_argument(
    "proxy_pass_url",
    type=str,
    required=False,
    help="The server will send the requst to this url.",
)

site_user_update_parser = site_target_parser.copy()
site_user_update_parser.add_argument("uuids", action="append", default=[], type=int)

custom_header_target_parser = authentication_parser.copy()
custom_header_target_parser.add_argument("custom_header_id", type=int, required=True)

create_custom_header_parser = site_target_parser.copy()
create_custom_header_parser.add_argument("header_name", required=True)
create_custom_header_parser.add_argument("header_content", required=True)

change_custom_header_parser = site_target_parser.copy()
change_custom_header_parser.add_argument("custom_header_id", type=int, required=True)
change_custom_header_parser.add_argument("header_name", required=False)
change_custom_header_parser.add_argument("header_content", required=False)