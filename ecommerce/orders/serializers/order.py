# pylint: disable=C0111
'''
Creación de serializadores relacionados con los Modelos de la aplicación
'''
import decimal

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.db import transaction

from ecommerce.orders.models.order import Order, OrderLog
from ecommerce.products.models.product import Product
from ecommerce.orders.serializers.order_detail import OrderDetailSerializer

class OrderSerializer(serializers.ModelSerializer):
    '''
    Serializador creación de cuentas
    '''

    product_list = serializers.ListField(
        child=serializers.JSONField(binary=True), 
        write_only=True
    )
    
    user = serializers.SerializerMethodField(required=False)
    status = serializers.CharField(required=False)
    price = serializers.DecimalField(required=False, max_digits=14, decimal_places=5)
    iva = serializers.DecimalField(required=False, max_digits=14, decimal_places=5)
    price_total = serializers.DecimalField(required=False, max_digits=14, decimal_places=5)
    residue = serializers.DecimalField(required=False, max_digits=14, decimal_places=5)

    def get_user(self, obj):
        try:
            return f'{obj.user.first_name} {obj.user.first_name}'
        except:
            return None

    class Meta:
        model = Order
        fields = (
            'user',
            'status',
            'price',
            'iva',
            'price_total',
            'residue',
            'product_list',
        )

    @transaction.atomic
    def create(self, validated_data):
        '''
        Guardar registro en la tabla Casos PQR
        '''
        try:
            validated_data['user'] = self._kwargs.get('context', {}).get('request', {}).user
            product_list = validated_data.pop('product_list', [])
            price = 0
            iva = 0
            price_total = 0
                            
            order = super().create(validated_data)
            # calcula el totas de los productos pedidos
            for value in product_list:
                try:
                    amount_product = value.get('amount_product', 0)
                    product_id = value.get('product', 0)

                    product = Product.objects.get(pk=product_id)
                    price = price + product.price * amount_product
                    iva = iva + product.iva * amount_product
                    price_total = price_total + (product.price_total * amount_product)
                    
                    data_detail_order = {
                        'user': validated_data['user'].id,
                        'product': product.id,
                        'order': order.id,
                        'amount': decimal.Decimal(amount_product)
                    }
                    order_detail_serializer = OrderDetailSerializer(data=data_detail_order) 
                    if order_detail_serializer.is_valid():
                        order_detail_serializer.save()
                    else:
                        raise serializers.ValidationError(order_detail_serializer.errors)
                except Product.DoesNotExist as error:
                    raise ValidationError(error)

            order.price = price
            order.iva = iva
            order.price_total = price_total
            order.residue = price_total
            order.save()
            
            return order
        except ValidationError as error:
            raise ValidationError(error)
    


class OrderLogSerializer(serializers.ModelSerializer):
    '''
    Serializador para log de modelo transaccional de cuentas
    '''
    created_by__name = serializers.SerializerMethodField()

    def get_created_by__name(self, obj):
        return obj.created_by.username
    
    class Meta:
        model = OrderLog
        fields = '__all__'
