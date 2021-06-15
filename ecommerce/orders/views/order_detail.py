
from ecommerce.base.view import BaseViewSet
from ecommerce.orders.serializers.order_detail import OrderDetailSerializer, OrderDetailLogSerializer
from ecommerce.orders.models.order_detail import OrderDetail, OrderDetailLog


class OrderDetailViewSet(BaseViewSet):
    '''
    Vista Modelo Ordenes
    '''

    app_code = 'orders'
    permission_code = 'orderdetail'
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer
    deny_access = ['list', 'add', 'retrieve']

class OrderDetailLogViewSet(BaseViewSet):
    '''
    Vista Log Modelo Ordenes
    '''

    app_code = 'orders'
    permission_code = 'orderdetaillog'
    queryset = OrderDetailLog.objects.all()
    serializer_class = OrderDetailLogSerializer
    deny_access = ['list', 'add', 'retrieve']
