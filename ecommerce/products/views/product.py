
import django_filters.rest_framework
from django_filters import rest_framework as filters

from rest_framework.filters import OrderingFilter
from rest_framework import serializers, status
from rest_framework.decorators import action
from rest_framework.response import Response

from ecommerce.base.view import BaseViewSet
from ecommerce.products.serializers.product import ProductSerializer, ProductLogSerializer
from ecommerce.products.models.product import Product, ProductLog


class ProductViewSet(BaseViewSet):
    """
    Vista Modelo Cuentas
    Cuales metodos tendran acceso libre.
    ['list', 'add', 'retrieve', 'change', 'delete']
    free_access : list = []
    Cuales metodos estan prohibidos.
    ['list', 'add', 'retrieve', 'change', 'delete']
    deny_access : list = []
    """

    app_code = 'products'
    permission_code = 'product'
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    free_access = ['list']
    deny_access = []

class ProductLogViewSet(BaseViewSet):
    '''
    Vista Modelo Cuentas
    '''

    app_code = 'products'
    permission_code = 'productlog'
    queryset = ProductLog.objects.all()
    serializer_class = ProductLogSerializer
    deny_access = ['retrieve', 'change', 'delete']
