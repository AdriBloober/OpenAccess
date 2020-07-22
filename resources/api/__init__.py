from flask_restplus import Api

from resources.config import config
from resources.errors import OpenAccessError

api = Api(
    title="OpenAccess",
    description="Access management for developer or deployed websites.",
    version=config.DEPLOYING_VERSION,
)


@api.errorhandler(OpenAccessError)
def api_error_handler(e: OpenAccessError):
    return {"status": "error", "error": e.__dict__()}, e.http_response
