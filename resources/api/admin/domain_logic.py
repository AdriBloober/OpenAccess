from resources.database.dtos.user import User
from resources.errors.authentication_errors import AccessDeniedError


def check_admin(user: User) -> User:
    if not user.admin:
        raise AccessDeniedError()
    else:
        return user
