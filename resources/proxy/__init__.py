import requests
from sqlalchemy.orm.exc import NoResultFound

from resources import app
from resources.api.admin.domain_logic import check_admin
from resources.api.authentication.domain_logic import get_session
from resources.database.dtos.site import Site

from flask import request, Response, abort

from resources.errors.authentication_errors import InvalidSessionError
from resources.proxy.proxy_error import SiteWasNotFound


@app.route("/<path:path>")
def proxy_route(path):
    try:
        token = ""
        if "OpenAccessToken" in request.cookies:
            token = request.cookies["OpenAccessToken"]
        elif "OpenAccessToken" in request.headers:
            token = request.headers["OpenAccessToken"]
        user = get_session(token)
        site = Site.query.filter(Site.host == request.host.lower()).one()
        if not (user in site.users or check_admin(user, raise_error=False)):
            raise InvalidSessionError()
        h = dict(request.headers)
        h["X-Real-Ip"] = request.remote_addr
        req = requests.request(
            request.method,
            f"{site.proxy_pass_url}/{path}",
            headers=request.headers,
            cookies=request.cookies,
            data=request.data,
            auth=request.authorization,
        )
        resp = Response(req.content, req.status_code, dict(req.headers))
        return resp
    except NoResultFound:
        abort(404)
    except requests.exceptions.ConnectionError:
        abort(502)
    except InvalidSessionError:
        abort(403)


@app.route("/")
def proxy_route_index():
    return proxy_route("")
