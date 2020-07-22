from flask_restplus import reqparse

authentication_parser = reqparse.RequestParser()
authentication_parser.add_argument(
    "OpenAccessToken", type=str, required=True, location=("cookies", "headers", "values", "json")
)

login_parser = reqparse.RequestParser()
login_parser.add_argument("name", type=str, required=True, help="The name of the user.")
login_parser.add_argument(
    "password", type=str, required=True, help="The password of the user."
)
