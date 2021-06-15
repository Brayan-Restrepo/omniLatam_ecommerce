"""Rides URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from ecommerce.products.views.product import ProductViewSet, ProductLogViewSet

router = DefaultRouter()
router.register(r'product', ProductViewSet, basename='product')
router.register(r'productlog', ProductLogViewSet, basename='productlog')

urlpatterns = [
    path('', include(router.urls))
]
