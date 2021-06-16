# pylint: disable=C0111
'''
Creación y administración de los modelos para gestión de CRM
- Definición de tuplas por modelo
- Definición de reglas de negocio por modelo
'''
from django.db import models
from rest_framework.exceptions import ValidationError

from ecommerce.base.model import BaseLogModel, BaseModel
from ecommerce.users.models.users import User
from ecommerce.products.models.product import Product
from ecommerce.orders.models.order import Order


class OrderDetailLog(BaseLogModel):
    '''Log modelo transaccional de detalle de ordenes'''
    record = models.ForeignKey('OrderDetail', verbose_name='Registro', on_delete=models.PROTECT)

    class Meta:
        permissions = (('retrieve_orderdetaillog', 'Can retrieve OrderDetaillog data'),
                       ('list_orderdetaillog', 'Can list OrderDetaillog data'))


class OrderDetail(BaseModel):
    '''Modelo para la gestión de detalle de ordenes'''
    log_class = OrderDetailLog

    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Cliente', null=False, blank=False, related_name='order_detail_user')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='Producto', null=False, blank=False, related_name='order_detail_product')
    order = models.ForeignKey(Order, on_delete=models.PROTECT, verbose_name='Orden', null=False, blank=False, related_name='order_detail_order')
    amount = models.DecimalField('Cantidad', max_digits=4, decimal_places=0, null=False, blank=False)
    price = models.DecimalField('Precio', max_digits=14, decimal_places=5, null=False, blank=False)
    iva = models.DecimalField('IVA', max_digits=14, decimal_places=5, null=False, blank=False)
    price_total = models.DecimalField('Precion + IVA', max_digits=14, decimal_places=5, null=False, blank=False)
    name_product = models.CharField('Nombre del producto', max_length=200, null=False, blank=False)
    supplier = models.CharField('Proveedor del producto', max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name_product

    class Meta:
        permissions = (('retrieve_orderdetail', 'Can retrieve orderdetail data'),
                       ('list_orderdetail', 'Can list orderdetail data'))


    def save(self, *args, **kwargs):
        try:
            self.price = self.product.price
            self.iva = self.product.iva
            self.price_total = self.product.price_total
            self.name_product = self.product.name
            self.supplier = self.product.supplier
            self.product.stock = self.product.stock - self.amount
            self.product.save()
            super().save(*args, **kwargs)

        except Exception as e:
            print('error')
            raise ValidationError(e)
