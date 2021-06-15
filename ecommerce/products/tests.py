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

# class MemberInvitationsAPITestCase(APITestCase):
#     """Member invitation API test case."""

#     def setUp(self):
#         """Test case setup."""
#         self.user = User.objects.create(
#             first_name='Pablo',
#             last_name='Trinidad',
#             email='pablotrinidad@ciencias.unam.mx',
#             username='pablotrinidad',
#             password='admin123'
#         )
#         self.profile = Profile.objects.create(user=self.user)
#         self.circle = Circle.objects.create(
#             name='Facultad de Ciencias',
#             slug_name='fciencias',
#             about='Grupo oficial de la Facultad de Ciencias de la UNAM',
#             verified=True
#         )
#         self.membership = Membership.objects.create(
#             user=self.user,
#             profile=self.profile,
#             circle=self.circle,
#             remaining_invitations=10
#         )

#         # Auth
#         self.token = Token.objects.create(user=self.user).key
#         self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(self.token))

#         # URL
#         self.url = '/circles/{}/members/{}/invitations/'.format(
#             self.circle.slug_name,
#             self.user.username
#         )

#     def test_response_success(self):
#         """Verify request succeed."""
#         request = self.client.get(self.url)
#         self.assertEqual(request.status_code, status.HTTP_200_OK)

#     def test_invitation_creation(self):
#         """Verify invitation are generated if none exist previously."""
#         # Invitations in DB must be 0
#         self.assertEqual(Invitation.objects.count(), 0)

#         # Call member invitations URL
#         request = self.client.get(self.url)
#         self.assertEqual(request.status_code, status.HTTP_200_OK)

#         # Verify new invitations were created
#         invitations = Invitation.objects.filter(issued_by=self.user)
#         self.assertEqual(invitations.count(), self.membership.remaining_invitations)
#         for invitation in invitations:
#             self.assertIn(invitation.code, request.data['invitations'])
