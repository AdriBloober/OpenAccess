from resources.errors import OpenAccessError


class AdminError(OpenAccessError):
    name = "admin_error"
    description = "On performing an action in the admin section, a error occured."
    http_response = 404


class SiteNameAlreadyExistsError(AdminError):
    name = "site_name_already_exists_error"
    description = "A site with this name already exists."


class SiteHostAlreadyExistsError(AdminError):
    name = "site_host_already_exists_error"
    description = "A site with this host already exists."


class SiteWasNotFoundError(AdminError):
    name = "site_was_not_found_error"
    description = "The requested site was not found and does not exists."
    http_response = 404


class HeaderWasNotFoundError(AdminError):
    name = "header_was_not_found_error"
    description = "The requested header was not found and does not exists."
    http_response = 404
