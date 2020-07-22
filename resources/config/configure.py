from os import environ


class ConfigObject:
    pass


class ConfigException(Exception):
    pass


class ArgumentIsRequiredError(ConfigException):
    def __init__(self, argument_name):
        super().__init__(f"The argument {argument_name} is required!")
        self.argument_name = argument_name


class TypeIsNotParsable(ConfigException):
    def __init__(self, t):
        self.type = t
        super().__init__(f"The type {t} is not parsable!")


REQUIRED_ARGUMENT = "Argument is required!"

PARSABLE_TYPES = [str, int, float, bool, None]


def get_config_object_from_json(c, o, prefixes=None):
    if prefixes is None:
        prefixes = []
    c = c()
    for k in dir(c):
        if k.startswith("_") or callable(getattr(c, k)):
            continue
        if k in o:
            v = o[k]
            n = "_".join(prefixes) + "_" + k
            if n.startswith("_"):
                n = n[1:]
            if environ.get(n, None) not in (None, ""):
                v = environ.get(n)
            if hasattr(c, "__annotations__") and k in c.__annotations__:
                t = c.__annotations__[k]
                if type(v) == dict and t != dict:
                    v = get_config_object_from_json(t, v, prefixes=prefixes + [k])
            if type(v) == str and v in ("true", "yes", "false", "no"):
                v = v in ("true", "yes")
            setattr(c, k, v)
        elif getattr(c, k) == REQUIRED_ARGUMENT:
            raise ArgumentIsRequiredError(k)
    return c


def get_json_from_config_object(o):
    if type(o) in (tuple, set):
        o = list(o)
    if not isinstance(o, ConfigObject):
        if type(o) == list:
            b = []
            for i in o:
                b.append(get_json_from_config_object(i))
            return b
        elif type(o) == dict:
            j = {}
            for k, v in o.items():
                j[k] = get_json_from_config_object(v)
            return j
        if type(o) not in PARSABLE_TYPES and o is not None:
            raise TypeIsNotParsable(type(o))
        return o
    j = {}
    ignore = []
    if hasattr(o, "__ignored_attributes__"):
        ignore.extend(o.__ignored_attributes__)
    for i in dir(o):
        if not i.startswith("_") and i not in ignore and not callable(getattr(o, i)):
            j[i] = get_json_from_config_object(getattr(o, i))
    return j
