from resources.errors import OpenAccessError


class AuthenticationError(OpenAccessError):
    name = "authentication_error"
    description = "On performing an action, a authentication error occured."
    http_response = 403


class UsernameAlreadyExistsError(AuthenticationError):
    name = "username_already_exists_error"
    description = "The username already exists"
    http_response = 400


class InvalidCredentialsError(AuthenticationError):
    name = "invalid_credentials_error"
    description = "The credentials to perform this authentication action are invalid."


class AccessDeniedError(AuthenticationError):
    name = "access_denied_error"
    description = "You don't have the required permissions to perform this action."


class InvalidSessionError(AuthenticationError):
    name = "invalid_session_error"
    description = (
            "The session is invalid or expired. You must reauthenticate you to perform this action with a new "
            "session. "
    )
    http_response = 401


class InvalidPasswordLinkError(AuthenticationError):
    name = "invalid_password_link_error"
    description = "The password link is invalid."
    http_response = 404


class UserWasNotFoundError(AuthenticationError):
    name = "user_was_not_found"
    description = "The target user was not found."
    http_response = 404
