import logging
import string
from os.path import exists

import yaml
from yaml import dump, load

from resources.config.configure import (
    ConfigObject,
    get_config_object_from_json,
    get_json_from_config_object,
)


class DatabaseConnectionConfig(ConfigObject):
    TYPE = "mysql+pymysql"
    HOST = "localhost"
    PORT = 3306
    USER = "access"
    PASSWORD = "access"
    DB = "access"
    ADDITIONAL_URI = ""


# Flask Configuration object
class FlaskConfig(ConfigObject):
    __ignored_attributes__ = ["SQLALCHEMY_DATABASE_URI"]
    FLASK_ENVIRONMENT = "production"
    DEBUG = False
    TESTING = False
    DATABASE: DatabaseConnectionConfig = DatabaseConnectionConfig()
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    PROPAGATE_EXCEPTIONS = False
    ERROR_INCLUDE_MESSAGE = False

    def __init__(self):
        self.SQLALCHEMY_DATABASE_URI = f"{self.DATABASE.TYPE}://{self.DATABASE.USER}:{self.DATABASE.PASSWORD}@{self.DATABASE.HOST}:{self.DATABASE.PORT}/{self.DATABASE.DB}{self.DATABASE.ADDITIONAL_URI}"


class TokenGeneratingConfig(ConfigObject):
    CHARSET = string.ascii_letters + "1234567890"
    LENGTH = 35

class SaltGeneratingConfig(ConfigObject):
    CHARSET = string.ascii_letters + "1234567890"
    LENGTH = 30

class AuthenticationConfig(ConfigObject):
    TOKEN_GENERATING_CONFIG: TokenGeneratingConfig = TokenGeneratingConfig()
    SALT_GENERATING_CONFIG: SaltGeneratingConfig = SaltGeneratingConfig()
    HASHING_MODE = "sha256"


class Config(ConfigObject):
    HTTP: FlaskConfig = FlaskConfig()
    AUTHENTICATION: AuthenticationConfig = AuthenticationConfig()
    DEPLOYING_VERSION = "0.1"


def write_config(c):
    with open("config.yml", "w") as file:
        file.write(dump(get_json_from_config_object(c)))


def get_config():
    if exists("config.yml"):
        with open("config.yml", "r") as file:
            c = get_config_object_from_json(Config, load(file, Loader=yaml.FullLoader))
        return c
    else:
        c = Config()
        write_config(c)
        return c


def parse_config():
    if config.HTTP.FLASK_ENVIRONMENT not in ("development", "production"):
        raise ValueError(
            "You must set the HTTP_ENVIRONMENT config variable to 'development' or 'production'!"
        )
    if config.HTTP.FLASK_ENVIRONMENT == "development":
        logging.warning("Development mode is enabled! Do not use in PRODUCTION!")


config: Config = get_config()
