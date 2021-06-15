# pylint: disable=C0111
'''
Creación de serializadores relacionados con los Modelos de la aplicación
'''
from rest_framework import serializers
from ecommerce.orders.models.order_detail import OrderDetail, OrderDetailLog

class OrderDetailSerializer(serializers.ModelSerializer):
    '''
    Serializador transaccional de detalle de ordenes
    '''
    
    price = serializers.DecimalField(required=False, max_digits=14, decimal_places=5, read_only=True)
    iva = serializers.DecimalField(required=False, max_digits=14, decimal_places=5, read_only=True)
    price_total = serializers.DecimalField(required=False, max_digits=14, decimal_places=5, read_only=True)
    name_product = serializers.CharField(required =False, max_length=200, read_only=True)
    supplier = serializers.CharField(required =False, max_length=200, read_only=True)
    
    def get_user(self, obj):
        try:
            return f'{obj.user.first_name} {obj.user.first_name}'
        except:
            return None

    class Meta:
        model = OrderDetail
        fields = (
            'user',
            'product',
            'order',
            'amount',
            'price',
            'iva',
            'price_total',
            'name_product',
            'supplier',
        )

class OrderDetailLogSerializer(serializers.ModelSerializer):
    '''
    Serializador para log de modelo transaccional de detalle de ordenes
    '''
    created_by__name = serializers.SerializerMethodField()

    def get_created_by__name(self, obj):
        return obj.created_by.username
    
    class Meta:
        model = OrderDetailLog
        fields = '__all__'
