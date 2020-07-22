class OpenAccessError(Exception):
    name = "open_access_error"
    description = "Basic OpenAccess error."
    http_response = 500

    def __dict__(self, disable_parent=False):
        j = {"name": self.name, "description": self.description}
        base = self.__class__.__base__
        if not disable_parent and base and base not in (OpenAccessError, Exception):
            j["parent"] = base().__dict__(disable_parent=True)
        return {"name": self.name, "description": self.description}
