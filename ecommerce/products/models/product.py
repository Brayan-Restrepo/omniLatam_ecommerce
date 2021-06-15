# pylint: disable=C0111
'''
Creación y administración de los modelos para gestión de CRM
- Definición de tuplas por modelo
- Definición de reglas de negocio por modelo
'''
from django.db import models
from rest_framework.exceptions import ValidationError
from ecommerce.base.model import BaseLogModel, BaseModel

DISPONIBLE = 'DISPONIBLE'
AGOTADO = 'AGOTADO'

STATUS = [
    (DISPONIBLE, 'DISPONIBLE'),
    (AGOTADO, 'AGOTADO'),
]

class ProductLog(BaseLogModel):
    '''Log modelo transaccional de productos'''
    record = models.ForeignKey('Product', verbose_name='Registro', on_delete=models.PROTECT)

    class Meta:
        permissions = (('retrieve_productlog', 'Can retrieve Productlog data'),
                       ('list_productlog', 'Can list Productlog data'))


class Product(BaseModel):
    '''Modelo para la gestión de productos'''
    log_class = ProductLog

    code = models.CharField('Codigo', max_length=20, null=False, blank=False, unique=True)
    name = models.CharField('Nombre', max_length=200, null=False, blank=False, unique=True)
    description = models.CharField('Descripción', max_length=5000, null=True, blank=True)
    supplier = models.CharField('Proveedor', max_length=200, null=True, blank=True)
    status = models.CharField('Estado', max_length=200, choices=STATUS, null=True, blank=True)
    stock = models.DecimalField('Cantidad', max_digits=4, decimal_places=0, null=True, blank=True)
    price = models.DecimalField('Precio', max_digits=14, decimal_places=5, null=False, blank=False)
    iva = models.DecimalField('IVA', max_digits=14, decimal_places=5, null=False, blank=False)
    price_total = models.DecimalField('Precion + IVA', max_digits=14, decimal_places=5, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        permissions = (('retrieve_product', 'Can retrieve product data'),
                       ('list_product', 'Can list product data'))


    def save(self, *args, **kwargs):
        try:
            if (not self.stock is None  and self.stock > 0):
                self.status = DISPONIBLE
            elif self.stock < 0:
                raise ValidationError(f'No hay stock disponible del producto {self.name}')
            else:
                self.stock = 0
                self.status = AGOTADO
            self.price_total = self.price + self.iva
            super().save(*args, **kwargs)
        except Exception as e:
            print('error')
            raise ValidationError(e)
