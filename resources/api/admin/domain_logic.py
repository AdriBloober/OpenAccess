from copy import deepcopy
from typing import List

from sqlalchemy.orm.exc import NoResultFound

from resources import database
from resources.api.authentication.domain_logic import get_user_by_id
from resources.database.dtos.site import Site
from resources.database.dtos.site_custom_header import SiteCustomHeader
from resources.database.dtos.user import User
from resources.errors.admin_errors import (
    SiteNameAlreadyExistsError,
    SiteHostAlreadyExistsError,
    SiteWasNotFoundError,
    HeaderWasNotFoundError,
)
from resources.errors.authentication_errors import AccessDeniedError


def check_admin(user: User, raise_error=True) -> User:
    if not user.admin:
        if raise_error:
            raise AccessDeniedError()
        else:
            return False
    else:
        return user


def check_site_name_exists(name):
    try:
        Site.query.filter(Site.name == name).one()
        raise SiteNameAlreadyExistsError()
    except NoResultFound:
        return


def check_site_host_exists(host):
    try:
        Site.query.filter(Site.host == host).one()
        raise SiteHostAlreadyExistsError()
    except NoResultFound:
        return


def get_site_by_id(site_id):
    try:
        return Site.query.filter(Site.id == site_id).one()
    except NoResultFound:
        raise SiteWasNotFoundError()


def create_site(name, host, proxy_pass_url) -> Site:
    name = name.lower()
    host = host.lower()
    check_site_name_exists(name)
    check_site_host_exists(host)
    site = Site(name, host, proxy_pass_url)
    database.add(site, commit=False)
    create_custom_header(site, "X-Real-Ip", "request.remote_addr")
    database.db.session.commit()
    return site


def delete_site(site: Site):
    database.remove(site)


def add_user_to_site(site, user):
    site.users.append(user)
    database.db.session.commit()


def remove_user_from_site(site, user):
    try:
        site.users.remove(user)
        database.db.session.commit()
    except ValueError:
        pass


def change_users_site(site: Site, list_of_uuids: List[int]):
    list_of_uuids = deepcopy(list_of_uuids)
    for user in site.users:
        if user.id not in list_of_uuids:
            site.users.remove(user)
        else:
            list_of_uuids.remove(user.id)
    for uuid in list_of_uuids:
        site.users.append(get_user_by_id(uuid))
    database.db.session.commit()


def update_site_values(site, host=None, proxy_pass_url=None):
    if host:
        host = host.lower()
    if host and site.host != host:
        check_site_host_exists(host)
        site.host = host
    if proxy_pass_url:
        site.proxy_pass_url = proxy_pass_url
    database.db.session.commit()


def create_custom_header(site, name, value):
    header = SiteCustomHeader(name, value, site)
    database.add(header)
    return header


def change_custom_header(header, name=None, value=None) -> SiteCustomHeader:
    if name:
        header.header_name = name
    if value:
        header.header_content = value
    database.db.session.commit()
    return header


def get_header_by_id(header_id: int):
    try:
        return SiteCustomHeader.query.filter(SiteCustomHeader.id == header_id).one()
    except NoResultFound:
        raise HeaderWasNotFoundError()


def remove_header(header: SiteCustomHeader):
    if header.site:
        header.site.custom_headers.remove(header)
    database.remove(header)
