from flask_restplus import reqparse

authentication_parser = reqparse.RequestParser()
authentication_parser.add_argument(
    "OpenAccessToken",
    type=str,
    required=True,
    location=("cookies", "headers", "values", "json"),
)

login_parser = reqparse.RequestParser()
login_parser.add_argument("name", type=str, required=True, help="The name of the user.")
login_parser.add_argument(
    "password", type=str, required=True, help="The password of the user."
)

password_link_parser = authentication_parser.copy()
password_link_parser.add_argument("token", type=str, required=True)

password_link_perform = password_link_parser.copy()
password_link_perform.add_argument("new_password", type=str, required=True)

password_change_parser = authentication_parser.copy()
password_change_parser.add_argument("current_password", type=str, required=False)
password_change_parser.add_argument("new_password", type=str, required=True)
