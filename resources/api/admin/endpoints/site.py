from flask_restplus import Resource

from resources.api import api
from resources.api.admin import namespace
from resources.api.admin.api_definition import site_with_users, custom_header_with_site
from resources.api.admin.domain_logic import (
    check_admin,
    create_site,
    get_site_by_id,
    delete_site,
    add_user_to_site,
    remove_user_from_site,
    change_users_site,
    update_site_values,
    get_header_by_id,
    create_custom_header,
    change_custom_header,
    remove_header,
)
from resources.api.admin.parsers import (
    site_creation_parser,
    site_target_parser,
    site_user_update_parser,
    site_changing_parser,
    custom_header_target_parser,
    create_custom_header_parser,
    change_custom_header_parser,
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

    @api.expect(site_changing_parser)
    @api.marshal_with(site_with_users)
    def put(self):
        args = site_changing_parser.parse_args()
        check_admin(get_session(args["OpenAccessToken"]))
        site = get_site_by_id(args["site_id"])
        update_site_values(
            site, host=args["host"], proxy_pass_url=args["proxy_pass_url"]
        )
        return site


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


@namespace.route("/site/custom_headers")
class CustomHeaderResource(Resource):
    @api.expect(custom_header_target_parser)
    @api.marshal_with(custom_header_with_site)
    def get(self):
        args = custom_header_target_parser.parse_args()
        check_admin(get_session(args["OpenAccessToken"]))
        return get_header_by_id(args["custom_header_id"])

    @api.expect(create_custom_header_parser)
    @api.marshal_with(custom_header_with_site)
    def post(self):
        args = create_custom_header_parser.parse_args()
        check_admin(get_session(args["OpenAccessToken"]))
        site = get_site_by_id(args["site_id"])
        header = create_custom_header(site, args["header_name"], args["header_content"])
        return header

    @api.expect(change_custom_header_parser)
    @api.marshal_with(custom_header_with_site)
    def put(self):
        args = change_custom_header_parser.parse_args()
        check_admin(get_session(args["OpenAccessToken"]))
        return change_custom_header(
            get_header_by_id(args["custom_header_id"]),
            name=args["header_name"],
            value=args["header_content"],
        )

    @api.expect(custom_header_target_parser)
    def delete(self):
        args = custom_header_target_parser.parse_args()
        check_admin(get_session(args["OpenAccessToken"]))
        remove_header(get_header_by_id(args["custom_header_id"]))
        return {"status": "success"}
