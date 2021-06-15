# pylint: disable=C0111
'''
Creación de serializadores relacionados con los Modelos de la aplicación
'''
import decimal

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.db import transaction

from ecommerce.orders.models.transactions import Transactions, TransactionsLog
from ecommerce.orders.models.order import Order

class TransactionsSerializer(serializers.ModelSerializer):
    '''
    Serializador transaccional de detalle de ordenes
    '''
    
    order_list = serializers.ListField(
        child=serializers.JSONField(binary=True), 
        write_only=True
    )
    order = serializers.SerializerMethodField(required=False, read_only=True)
    payment = serializers.DecimalField(required=False, max_digits=14, decimal_places=5, read_only=True)
    residue = serializers.DecimalField(required=False, max_digits=14, decimal_places=5, read_only=True)

    def get_order(self, obj):
        try:
            return f'{obj.order.status}'
        except:
            return None


    class Meta:
        model = Transactions
        fields = (
            'order_list',
            'order',
            'payment_method',
            'payment',
            'residue',
            'code_transactions',
        )

    @transaction.atomic
    def create(self, validated_data):
        '''
        Guardar registro transacciones
        '''
        try:
            order_list = validated_data.pop('order_list', [])
                        
            # calcula el totas de los productos pedidos
            for value in order_list:
                try:
                    payment = decimal.Decimal(value.get('payment', 0))
                    order_id = value.get('order', 0)
                    order = Order.objects.get(pk=order_id)
                    order.residue = order.residue - payment
                    order.save()
                    
                    validated_data['order'] = order
                    validated_data['payment'] = payment
                    validated_data['residue'] = order.residue
                    transactions = super().create(validated_data)
                except Order.DoesNotExist as error:
                    raise ValidationError(error)
            
            return transactions
        except ValidationError as error:
            raise ValidationError(error)
    
class TransactionsLogSerializer(serializers.ModelSerializer):
    '''
    Serializador para log de modelo transaccional de detalle de ordenes
    '''
    created_by__name = serializers.SerializerMethodField()

    def get_created_by__name(self, obj):
        return obj.created_by.username
    
    class Meta:
        model = TransactionsLog
        fields = '__all__'
