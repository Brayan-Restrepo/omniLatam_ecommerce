from django.http import HttpRequest

from rest_framework.response import Response


def validate_permission(access : str, view : object, request : HttpRequest) -> bool:
    try:
        # Validar si el acceso esta restringido.
        if access in view.deny_access:
            return Response({'detail': ['Acceso inválido.']}, status=403)

        # Validar si el acceso esta en la lista de acceso libre.
        if access in view.free_access:
            return True

        # Formar el string completo del permiso.
        permission_name_app : str = '{}.{}_{}'.format(view.app_code, access, view.permission_code)
        if not request.user.has_perm(permission_name_app):
            return Response({'detail': ['Acceso inválido.']}, status=403)
    except AttributeError:
        return Response({'detail': ['Acceso inválido.']}, status=403)
    except Exception:
        return Response({'detail': ['Error inesperado validando permisos.']}, status=402)

    return True
