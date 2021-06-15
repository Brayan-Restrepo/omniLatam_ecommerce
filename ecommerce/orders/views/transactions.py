
from ecommerce.base.view import BaseViewSet
from ecommerce.orders.serializers.transactions import TransactionsSerializer, TransactionsLogSerializer
from ecommerce.orders.models.transactions import Transactions, TransactionsLog


class TransactionsViewSet(BaseViewSet):
    '''
    Vista Modelo Ordenes
    '''
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
    permission_code = 'transactions'
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer
    deny_access = ['change', 'delete']

class TransactionsLogViewSet(BaseViewSet):
    '''
    Vista Log Modelo Ordenes
    '''

    app_code = 'orders'
    permission_code = 'transactionslog'
    queryset = TransactionsLog.objects.all()
    serializer_class = TransactionsLogSerializer
    deny_access = ['change', 'delete']
