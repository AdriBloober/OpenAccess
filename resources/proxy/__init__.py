import requests
from sqlalchemy.orm.exc import NoResultFound

from resources import app
from resources.api.admin.domain_logic import check_admin
from resources.api.authentication.domain_logic import get_session
from resources.database.dtos.site import Site

from flask import request, Response, abort

from resources.errors.authentication_errors import InvalidSessionError
from resources.proxy.proxy_error import SiteWasNotFound


def parse_header_content(content) -> str:
    if content is None:
        return ""
    if type(content) in (int, float):
        return str(content)
    if content.lower().startswith("request."):
        return getattr(request, "request.asdf".join(content.split("request.")[1:]))
    return content


@app.route("/<path:path>", methods=["GET", "POST", "DELETE", "PUT"])
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

        for custom_header in site.custom_headers:
            h[custom_header.header_name] = parse_header_content(
                custom_header.header_content
            )
        req = requests.request(
            request.method,
            f"{site.proxy_pass_url}/{path}",
            headers=h,
            cookies=request.cookies,
            data=request.data,
            params=request.args,
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


@app.route("/", methods=["GET", "POST", "DELETE", "PUT"])
def proxy_route_index():
    return proxy_route("")
