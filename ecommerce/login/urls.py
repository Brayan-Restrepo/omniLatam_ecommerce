# pylint: disable=C0111
'''
'''
from django.conf.urls import include, url

from .views import LoginAdminView, LoginView, LogoutView

app_name = 'login'

urlpatterns = [ # pylint: disable=C0103
    url(r'^account/$', LoginAdminView.as_view(), name='login_admin'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
]
