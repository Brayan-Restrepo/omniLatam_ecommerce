"""User model."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Utilities
# from ecommerce.base.model import BaseModel
from ecommerce.includes.validator import PHONE_REGEX

class User(AbstractUser):
    """User model.

    Extend from Django's Abstract User, change the username field
    to email and add some extra fields.
    """


    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'Un usuario con ese email ya existe.'
        }
    )

    phone_number = models.CharField(validators=[PHONE_REGEX], max_length=17, blank=True)

    is_client = models.BooleanField(
        'client',
        default=True,
        help_text=(
            'Ayude a distinguir fácilmente a los usuarios y a realizar consultas.'
            'Los clientes son el principal tipo de usuario.'
        )
    )

    is_verified = models.BooleanField(
        'verified',
        default=True,
        help_text='Establézcalo en verdadero cuando el usuario haya verificado su dirección de correo electrónico.'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        """Return username."""
        return self.username

    def get_short_name(self):
        """Return username."""
        return self.username
