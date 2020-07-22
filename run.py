import logging


from resources import app, config


class DeployProductionWithDeployingServiceError(Exception):
    def __init__(self):
        super().__init__(
            "If you want to run you'r OpenAccess application in production, you must use a deploying service like gunicorn!"
        )


if config.HTTP.FLASK_ENVIRONMENT != "development":
    raise DeployProductionWithDeployingServiceError()
logging.warning(
    "This is a development server: Use Gunicorn or other deploying services for deploying!"
)
app.run(host="127.0.0.1", port=8080)
