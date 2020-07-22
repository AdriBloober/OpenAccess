class ProxyError(Exception):
    pass


class SiteWasNotFound(ProxyError):
    def __init__(self):
        super().__init__("The requested site was not found.")
