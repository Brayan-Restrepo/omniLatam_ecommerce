# pylint: disable=C0111
'''
Creación de serializadores relacionados con los Modelos de la aplicación
'''
from rest_framework import serializers
from ecommerce.products.models.product import Product, ProductLog

class ProductSerializer(serializers.ModelSerializer):
    '''
    Serializador creación de cuentas
    '''
    
    class Meta:
        model = Product
        fields = (
            'code',
            'name',
            'description',
            'supplier',
            'stock',
            'price',
            'iva',
        )

class ProductLogSerializer(serializers.ModelSerializer):
    '''
    Serializador para log de modelo transaccional de cuentas
    '''
    created_by__name = serializers.SerializerMethodField()

    def get_created_by__name(self, obj):
        return obj.created_by.username
    
    class Meta:
        model = ProductLog
        fields = '__all__'
