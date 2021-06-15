# pylint: disable=C0111
'''
Vista del archivo login
'''
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from ecommerce.users.models.users import User
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings
from rest_framework.exceptions import ValidationError


class LoginView(APIView):
    '''
    Metodo para iniciar sesión.
    '''

    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        try:
            errors = {}
            email = request.data.get('email')
            password = request.data.get('password')

            if email == '' or email is None:
                errors['email'] = ['El campo email es obligatorio.']
            if password == '' or password is None:
                errors['password'] = ['El campo contraseña es obligatorio.']

            if len(errors) > 0:
                return Response(errors, status=status.HTTP_400_BAD_REQUEST)

            user = authenticate(email=email, password=password)
            if user is None:
                raise ValidationError({'detail': 'error'})
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            return Response(
                {
                    'staff': user.is_staff, 
                    'id': user.id, 
                    'token': 'JWT ' + token, 
                    'full_name': user.first_name + ' ' + user.last_name
                }, 
                status=status.HTTP_202_ACCEPTED
            )
        except Exception as e:
            print(e)
            return Response({'detail': ['Usuario o contraseña incorrectos.']}, status=status.HTTP_401_UNAUTHORIZED)

class LoginAdminView(View):
    '''
    Clase para iniciar sesión.
    '''
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name, {})

    def post(self, request):
        """
        Método que para iniciar session desde el administrador del api
        """
        try:
            email = request.POST.get('email')
            passwordl = request.POST.get('password')
            login_admin = 'login:login_admin'

            if email and passwordl:

                users = User.objects.get(email=email)
                user = authenticate(email=email, password=passwordl)

                if user is None:
                    raise ValidationError({'detail': 'error'})

                login(request, users)
                request.session.set_expiry(settings.SESSION_TIMEOUT)

                if not users.is_staff:
                    messages.error(request, 'El usuario es valido pero no tiene acceso al sitio de administración.')
                    return HttpResponseRedirect(reverse(login_admin))
                return HttpResponseRedirect(reverse('admin:index'))
            else:
                messages.error(request, 'Nombre de usuario y contraseña son obligatorios.')
                return HttpResponseRedirect(reverse(login_admin))
        except Exception as e:
            print(e)
            return Response({'detail': ['Usuario o contraseña incorrectos.']}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    '''
    Metodo para cerrar la sesión.
    '''

    def get(self, request):
        # El token llega con el formato "Toke <numero_token>" se ejecuta el split y se toma la segunda posicion...
        try:
            print('completar')
        except Token.DoesNotExist:
            return Response({'detail':['Token incorrecto']}, status=status.HTTP_401_UNAUTHORIZED)

        response = Response({}, status=status.HTTP_202_ACCEPTED)
        return response
