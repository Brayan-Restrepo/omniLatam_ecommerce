
from ecommerce.base.view import BaseViewSet
from ecommerce.orders.serializers.order import OrderSerializer, OrderLogSerializer
from ecommerce.orders.models.order import Order, OrderLog


class OrderViewSet(BaseViewSet):
    """
    Vista Modelo Ordenes
    Cuales metodos tendran acceso libre.
    ['list', 'add', 'retrieve', 'change', 'delete']
    free_access : list = []
    Cuales metodos estan prohibidos.
    ['list', 'add', 'retrieve', 'change', 'delete']
    deny_access : list = []
    """

    app_code = 'orders'
    permission_code = 'order'
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    deny_access = ['change', 'delete']

class OrderLogViewSet(BaseViewSet):
    '''
    Vista Log Modelo Ordenes
    '''

    app_code = 'orders'
    permission_code = 'orderlog'
    queryset = OrderLog.objects.all()
    serializer_class = OrderLogSerializer
    deny_access = ['list', 'add', 'retrieve']
