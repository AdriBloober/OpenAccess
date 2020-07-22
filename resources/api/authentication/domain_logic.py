import hmac
import random

from sqlalchemy.orm.exc import NoResultFound

from resources import database
from resources.config import config
from resources.database.dtos.password_link import PasswordLink
from resources.database.dtos.session import Session
from resources.database.dtos.user import User
from resources.errors.authentication_errors import (
    UsernameAlreadyExistsError,
    InvalidCredentialsError,
    InvalidSessionError,
    InvalidPasswordLinkError,
    UserWasNotFoundError,
)


def get_session_by_token(token):
    try:
        return Session.query.filter(Session.token == token).one()
    except NoResultFound:
        raise InvalidSessionError()


def generate_session_token(session_existing_checking=True):
    while True:
        token = ""
        while len(token) < config.AUTHENTICATION.TOKEN_GENERATING_CONFIG.LENGTH:
            token += random.choice(
                list(config.AUTHENTICATION.TOKEN_GENERATING_CONFIG.CHARSET)
            )
        if not session_existing_checking:
            return token
        try:
            get_session_by_token(token)
            continue
        except NoResultFound:
            return token


def generate_salt():
    salt = ""
    while len(salt) < config.AUTHENTICATION.SALT_GENERATING_CONFIG.LENGTH:
        salt += random.choice(
            list(config.AUTHENTICATION.SALT_GENERATING_CONFIG.CHARSET)
        )
    return salt


def get_user_by_name(name):
    return User.query.filter(User.name == name).one()


def create_user(name, admin=False):
    name = name.lower()
    try:
        get_user_by_name(name)
        raise UsernameAlreadyExistsError()
    except NoResultFound:
        user = User(name, None, None, admin=admin)
        database.add(user)
        return user


def hash_password_algorithm(password, salt=generate_salt()):
    h = hmac.new(
        salt.encode("utf-8"),
        password.encode("utf-8"),
        config.AUTHENTICATION.HASHING_MODE,
    )
    return h.hexdigest(), salt


def login(name, password) -> User:
    try:
        user = User.query.filter(User.name == name).one()
        if user.password == hash_password_algorithm(password, user.salt)[0]:
            return user
        else:
            raise InvalidCredentialsError()
    except NoResultFound:
        raise InvalidCredentialsError()


def create_session(user: User):
    session = Session(generate_session_token(), user)
    database.add(session)
    return session


def get_user_by_session(session: Session):
    return session.user


def get_session(token):
    return get_user_by_session(get_session_by_token(token))


def create_password_link(target_user: User):
    password_link = PasswordLink(
        generate_session_token(session_existing_checking=False)
        + generate_session_token(session_existing_checking=False),
        target_user,
    )
    database.add(password_link)
    return password_link


def get_password_link_by_token(token):
    try:
        return PasswordLink.query.filter(PasswordLink.token == token).one()
    except NoResultFound:
        raise InvalidPasswordLinkError()


def perform_password_link(password_link: PasswordLink, new_password) -> User:
    hashed_password, salt = hash_password_algorithm(new_password)
    user = password_link.user
    user.password = hashed_password
    user.salt = salt
    database.remove(password_link)
    return user


def logout(session: Session):
    database.remove(session)


def get_user_by_id(target_user_id: int):
    try:
        return User.query.filter(User.id == target_user_id).one()
    except NoResultFound:
        raise UserWasNotFoundError()


# TODO : Delete user from sites
def delete_user(target_user: User):
    database.remove(target_user)
