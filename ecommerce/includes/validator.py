# pylint: disable=C0111
'''
Django custom validations
'''
from django.core.validators import RegexValidator

INVALID = 'Inválido'

IS_ALPHANUMERICVALIDATOR = RegexValidator(
  regex=r'^[a-zA-Z0-9 ]*$',
  message='Este campo debe ser alfanumérico.',
  code=INVALID
)

IS_NUMBERVALIDATOR = RegexValidator(
  regex=r'^[0-9]*$',
  message='Este campo debe ser numérico.',
  code=INVALID
)

IS_LOWERVALIDATOR = RegexValidator(
  regex=r'^[a-z]*$',
  message='Este campo solo permite letras minúsculas.',
  code=INVALID
)

IS_NODIACRITICVALIDATOR = RegexValidator(
  regex=r'^[a-zA-Z]*$',
  message='Este campo no permite letras tildadas.',
  code=INVALID
)

IS_ALPHAVALIDATOR = RegexValidator(
  regex=r'^[a-zA-Z-ñÑ-áéíóúÁÉÍÓÚ/ ]+$',
  message='Este campo sólo permite letras.',
  code=INVALID
)

IS_LENGTH = RegexValidator(
  regex=r'^[0-9]{1,3}$',
  message='Este campo solo permite 3 dígitos',
  code=INVALID
)

IS_EMAIL = RegexValidator(
  regex=r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$",
  message='Este campo debe de ser un email',
  code=INVALID
)

PHONE_REGEX = RegexValidator(
  regex=r'\+?1?\d{9,15}$',
  message='El número de teléfono debe ingresarse en el formato: +999999999. Se permiten hasta 15 dígitos.',
  code=INVALID
)