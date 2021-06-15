'''
    custom_auth by Juan David González Bedoya
'''
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.backends import ModelBackend
from django.core.exceptions import ValidationError
from ecommerce.users.models.users import User

from rest_framework_jwt import utils
from django.conf import settings
import requests


class CustomBackend(ModelBackend):
    '''
    Autenticación personalizada, se deben definir dos metodos por lo menos
    authenticate()
    get_user()

    Documentación oficial
    https://docs.djangoproject.com/en/1.11/topics/auth/customizing/#specifying-authentication-backends

    Leer los siguientes títulos para entender el proceso
        - Specifying authentication backends
        - Writing an authentication backend
    '''

    def authenticate(self, request, username=None, password=None):
        '''
        Autenticar el usuario por aplicación o directorio activo.
        Se ejecuta cuando se llama el authenticate() del paquete django.contrib.auth.autehnticate
        y debe de estar configurado en el settings (lista llamada AUTHENTICATION_BACKENDS)

        request: objecto de la petición actual
        username: username que se envió por la petición
        password: password que se envió por la petición
        '''
        try:
            # Consultar el usuario en la aplicación solo por username
            user_exist_django = User.objects.select_related('user_data_user').get(username=username, user_data_user__deleted=False)
            if not user_exist_django.check_password(password):
                user_exist_django = None
            

        except User.DoesNotExist:
            # None cuando NO existe el usuario en aplicación
            user_exist_django = None
        except ObjectDoesNotExist:
            # None cuando no encuentra información en user_data
            user_exist_django = None      
        # Retornar la instancia encontrada o en su defecto un None
        return user_exist_django


def jwt_response_payload_handler(token, user=None, request=None):
    '''
    Personalizar los datos que se devolveran después de que un usuario se autentique
    por medio del jwt

    Se ejecuta después de que jwt autentique el usuario. Se configura en el settings,
    en el diccionario JWT_AUTH con clave JWT_RESPONSE_PAYLOAD_HANDLER

    Leer el siguiente link para entender el proceso
    https://getblimp.github.io/django-rest-framework-jwt/#additional-settings

    token:      token generado cuando el usuario se autentico
    user:       instancia del usuario autenticado
    request:    objeto de la petición actual
    '''

    # Info del usuario a retornar
    user_info = {
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'is_superuser': user.is_superuser
    }

    # Crear lista de permisos y consultar todos los grupos asociados al usuario
    permissions = []
    groups = user.groups.all()

    # Recorrer los grupos
    for group in groups:
        # Recorrer todos los permisos de cada grupo y asignarlos
        for permission in group.permissions.all():
            permissions.append(permission.codename)

    # Retornar el token y la info que deseas (Esta debe ser serializable)
    return {
        'token': token,
        'user': user_info,
        'permissions': permissions
    }


def jwt_payload_handler(user):
    payload = utils.jwt_payload_handler(user)

    return payload
