"""Rides URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from ecommerce.orders.views.order import OrderViewSet, OrderLogViewSet
from ecommerce.orders.views.order_detail import OrderDetailViewSet, OrderDetailLogViewSet
from ecommerce.orders.views.transactions import TransactionsViewSet, TransactionsLogViewSet

router = DefaultRouter()
router.register(r'order', OrderViewSet, basename='order')
router.register(r'orderlog', OrderLogViewSet, basename='orderlog')
router.register(r'orderdetail', OrderDetailViewSet, basename='orderdetail')
router.register(r'orderdetaillog', OrderDetailLogViewSet, basename='orderdetaillog')
router.register(r'transactions', TransactionsViewSet, basename='transactions')
router.register(r'transactionslog', TransactionsLogViewSet, basename='transactionslog')

urlpatterns = [
    path('', include(router.urls))
]
