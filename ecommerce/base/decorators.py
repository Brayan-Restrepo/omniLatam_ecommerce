from rest_framework.response import Response
from .defs import validate_permission

VIEW = 0
REQUEST = 1

def permission(action):
    def __permission(method):
        def inner(*args, **kwargs):
            permission = validate_permission(action, args[VIEW], args[REQUEST])
            if not permission is True:
                return permission
            return method(*args, **kwargs)
        return inner
    return __permission
