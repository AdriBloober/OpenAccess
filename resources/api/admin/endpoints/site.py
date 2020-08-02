from flask_restplus import Resource

from resources.api import api
from resources.api.admin import namespace
from resources.api.admin.api_definition import site_with_users
from resources.api.admin.domain_logic import (
    check_admin,
    create_site,
    get_site_by_id,
    delete_site,
    add_user_to_site,
    remove_user_from_site,
    change_users_site,
)
from resources.api.admin.parsers import (
    site_creation_parser,
    site_target_parser,
    site_user_update_parser,
)
from resources.api.authentication.domain_logic import get_session, get_user_by_id


@namespace.route("/sites")
class SitesResources(Resource):
    @api.expect(site_target_parser)
    @api.marshal_with(site_with_users)
    def get(self):
        args = site_target_parser.parse_args()
        check_admin(get_session(args["OpenAccessToken"]))
        return get_site_by_id(args["site_id"])

    @api.expect(site_creation_parser)
    @api.marshal_with(site_with_users)
    def post(self):
        args = site_creation_parser.parse_args()
        check_admin(get_session(args["OpenAccessToken"]))
        return create_site(args["name"], args["host"], args["proxy_pass_url"])

    @api.expect(site_target_parser)
    def delete(self):
        args = site_target_parser.parse_args()
        check_admin(get_session(args["OpenAccessToken"]))
        delete_site(get_site_by_id(args["site_id"]))
        return {"status": "success"}


@namespace.route("/site/users")
class SiteUserResource(Resource):
    @api.marshal_with(site_with_users)
    @api.expect(site_user_update_parser)
    def put(self):
        args = site_user_update_parser.parse_args()
        check_admin(get_session(args["OpenAccessToken"]))
        site = get_site_by_id(args["site_id"])
        change_users_site(site, args["uuids"])
        return site
