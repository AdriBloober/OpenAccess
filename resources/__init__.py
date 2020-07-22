from flask import Flask, Blueprint

from resources.api import api
from resources.config import config

app_initialized = False
app = Flask(__name__)


def set_app_config():
    app.config.from_object(config.HTTP)


def load_namespaces():
    from resources.api.authentication import namespace as authentication_namespace
    from resources.api.authentication.endpoints import sessions, users, password_link

    api.add_namespace(authentication_namespace)
    from resources.api.admin import namespace as admin_namespace
    from resources.api.admin.endpoints import users, password_link, site

    api.add_namespace(admin_namespace)


def initialize_api():
    from resources.api import api

    api_blueprint = Blueprint("api", __name__, url_prefix="/OpenAccess/api")
    api.init_app(api_blueprint)
    load_namespaces()
    app.register_blueprint(api_blueprint)


frontend_blueprint: Blueprint = None


def initialize_frontend():
    global frontend_blueprint
    frontend_blueprint = Blueprint("frontend", __name__, url_prefix="/OpenAccess")




def initialize_proxy():
    from resources import proxy


def initialize_app():

    global app_initialized
    if not app_initialized:
        app_initialized = True
        set_app_config()
        from resources import database

        database.setup()
        initialize_api()
        initialize_frontend()
        initialize_proxy()


initialize_app()
