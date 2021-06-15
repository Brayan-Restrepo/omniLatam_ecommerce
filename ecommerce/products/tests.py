from django.test import TestCase

# Create your tests here.

# Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase

# Model
from ecommerce.products.models.product import Product, ProductLog
from ecommerce.users.models.users import User
from rest_framework.authtoken.models import Token


DISPONIBLE = 'DISPONIBLE'
AGOTADO = 'AGOTADO'

class InvitationsManagerTestCase(TestCase):
    """Invitations manager test case."""

    def setUp(self):
        """Test case setup."""

    def test_product_disponible(self):
        """
        cuando el producto tiene stock > 0 el status es DISPONIBLE
        """
        product = Product.objects.create(
            code='AAA001',
            name='Nevera',
            description='Nevera ...........',
            supplier='Provedor',
            stock=18,
            price=5000.0,
            iva=150.0
        )
        self.assertEqual(product.status, DISPONIBLE)

    def test_product_agotado(self):
        """
        cuando el producto no tiene stock = 0 el status es AGOTADO
        """
        product = Product.objects.create(
            code='AAA001',
            name='Nevera',
            description='Nevera ...........',
            supplier='Provedor',
            stock=0.0,
            price=3000.0,
            iva=550.0
        )
        self.assertEqual(product.status, AGOTADO)
