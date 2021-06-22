# pylint: disable=C0111
'''
Creación y administración de los modelos para gestión de CRM
- Definición de tuplas por modelo
- Definición de reglas de negocio por modelo
'''
import decimal
from django.db import models
from ecommerce.base.model import BaseLogModel, BaseModel
from ecommerce.users.models.users import User
from ecommerce.includes.email import async_send_mail
from ..settings import PENDIENTE, ABONADO, PAGADO, STATUS

class OrderLog(BaseLogModel):
    '''Log modelo transaccional de ordenes'''
    record = models.ForeignKey('Order', verbose_name='Registro', on_delete=models.PROTECT)

    class Meta:
        permissions = (('retrieve_orderlog', 'Can retrieve Orderlog data'),
                       ('list_orderlog', 'Can list Orderlog data'))


class Order(BaseModel):
    '''Modelo para la gestión de ordenes'''
    log_class = OrderLog

    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Cliente', null=False, blank=False, related_name='order_user')
    status = models.CharField('Estado', max_length=200, choices=STATUS, null=True, blank=True)    
    price = models.DecimalField('Precio', max_digits=14, decimal_places=5, null=False, blank=False)
    iva = models.DecimalField('IVA', max_digits=14, decimal_places=5, null=False, blank=False)
    price_total = models.DecimalField('Precion + IVA', max_digits=14, decimal_places=5, null=False, blank=False)
    residue = models.DecimalField('Saldo', max_digits=14, decimal_places=5, null=False, blank=False)
    
    def __str__(self):
        return self.status

    class Meta:
        permissions = (('retrieve_order', 'Can retrieve order data'),
                       ('list_order', 'Can list order data'))


    def save(self, *args, **kwargs):
        try:
            if not self.status:
                self.status = PENDIENTE
                self.price = self.price if self.price else decimal.Decimal(0)
                self.iva = self.iva if self.iva else decimal.Decimal(0)
                self.price_total = self.price_total if self.price_total else decimal.Decimal(0)
                self.residue = self.residue if self.residue else decimal.Decimal(0)
            elif self.residue > 0 and self.residue < self.price_total:
                self.status = ABONADO
            elif self.residue <= 0 and self.status in [PENDIENTE, ABONADO]:
                self.status = PAGADO
                async_send_mail('Tu compra ha sido completada - OmniLatam', self.user, self.user.email)

            super().save(*args, **kwargs)
        except Exception as e:
            print('error')
            print(e)
