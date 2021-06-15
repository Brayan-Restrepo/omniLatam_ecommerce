from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = 'code', 'name', 'status', 'stock', 'price', 'price_total',

    search_fields = 'code', 'name', 'description',

    date_hierarchy = 'created_at'

    ordering = '-created_at',

    readonly_fields = 'id',

    list_filter = 'status', 'supplier',