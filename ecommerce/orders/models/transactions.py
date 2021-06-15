# pylint: disable=C0111
'''
Creación y administración de los modelos para gestión de CRM
- Definición de tuplas por modelo
- Definición de reglas de negocio por modelo
'''
from django.db import models
from ecommerce.base.model import BaseLogModel, BaseModel
from ecommerce.orders.models.order import Order


class TransactionsLog(BaseLogModel):
    '''Log modelo transaccional de detalle de ordenes'''
    record = models.ForeignKey('Transactions', verbose_name='Registro', on_delete=models.PROTECT)

    class Meta:
        permissions = (('retrieve_transactionslog', 'Can retrieve Transactionslog data'),
                       ('list_transactionslog', 'Can list Transactionslog data'))


class Transactions(BaseModel):
    '''Modelo para la gestión de detalle de ordenes'''
    log_class = TransactionsLog

    order = models.ForeignKey(Order, on_delete=models.PROTECT, verbose_name='Orden', null=False, blank=False, related_name='transactions_order')
    payment = models.DecimalField('Pago', max_digits=14, decimal_places=5, null=False, blank=False)
    payment_method = models.CharField('Metodo de pago', max_length=200, null=True, blank=True)
    residue = models.DecimalField('Saldo', max_digits=14, decimal_places=5, null=False, blank=False)
    code_transactions = models.CharField('Codigo de transacción', max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.name_product

    class Meta:
        permissions = (('retrieve_transactions', 'Can retrieve transactions data'),
                       ('list_transactions', 'Can list transactions data'))


    def save(self, *args, **kwargs):
        try:
            super().save(*args, **kwargs)
        except Exception as e:
            print('error')
            print(e)
