from django.test import TestCase

from ecommerce.users.models.users import User
from ecommerce.orders.models.order import Order
from ecommerce.orders.settings import PENDIENTE, ABONADO, PAGADO

class ProductTestCase(TestCase):
    """Invitations manager test case."""

    def setUp(self):
        """Test case setup."""
        self.user = User.objects.create(
            first_name='brayan',
            last_name='restrepo',
            email='brayan.restrepo@unillanos.edu.co',
            username='brayan.restrepo',
            password='brayan.restrepo'
        )
        self.order = Order.objects.create(
            user=self.user,
            price=500000.0,
            iva=10000.0,
            price_total=510000.0,
            residue=510000.0
        )

    def test_order_status_pendiente(self):
        """
        Cuando el saldo es igual al salo el estado es pendiente
        """
        self.assertEqual(self.order.status, PENDIENTE)

    def test_order_status_abonado(self):
        """
        Cuando el saldo es mayor a 0 y menor al total de la orden el estado es ABONADO
        """
        self.order.residue=5000.0
        self.order.save()
        self.assertEqual(self.order.status, ABONADO)

    def test_order_pagado(self):
        """
        Cuando el saldo es 0 el estado de la orden es pagado
        """
        self.order.residue=0.0
        self.order.save()
        self.assertEqual(self.order.status, PAGADO)
        
