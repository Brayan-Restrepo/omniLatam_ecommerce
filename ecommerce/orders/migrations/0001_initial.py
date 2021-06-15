# Generated by Django 3.2.4 on 2021-06-14 08:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0004_auto_20210612_2104'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha última de modificación')),
                ('is_active', models.BooleanField(default=True, verbose_name='Esta activo')),
                ('deleted', models.BooleanField(default=False, verbose_name='Eliminado')),
                ('status', models.CharField(blank=True, choices=[('PENDIENTE', 'PENDIENTE'), ('PAGADO', 'PAGADO'), ('PAGADO - ENVIADO', 'PAGADO - ENVIADO'), ('PAGADO - ENTREGADO', 'PAGADO - ENTREGADO'), ('CANCELADO', 'CANCELADO'), ('FINALIZADO', 'FINALIZADO')], max_length=200, null=True, verbose_name='Estado')),
                ('price', models.DecimalField(decimal_places=5, max_digits=9, verbose_name='Precio')),
                ('iva', models.DecimalField(decimal_places=5, max_digits=9, verbose_name='IVA')),
                ('price_total', models.DecimalField(decimal_places=5, max_digits=9, verbose_name='Precion + IVA')),
                ('residue', models.DecimalField(decimal_places=5, max_digits=9, verbose_name='Saldo')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orders_order_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orders_order_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Última modificación por')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order_user', to=settings.AUTH_USER_MODEL, verbose_name='Cliente')),
            ],
            options={
                'permissions': (('retrieve_order', 'Can retrieve order data'), ('list_order', 'Can list order data')),
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha última de modificación')),
                ('is_active', models.BooleanField(default=True, verbose_name='Esta activo')),
                ('deleted', models.BooleanField(default=False, verbose_name='Eliminado')),
                ('amount', models.DecimalField(decimal_places=0, max_digits=4, verbose_name='Cantidad')),
                ('price', models.DecimalField(decimal_places=5, max_digits=9, verbose_name='Precio')),
                ('iva', models.DecimalField(decimal_places=5, max_digits=9, verbose_name='IVA')),
                ('price_total', models.DecimalField(decimal_places=5, max_digits=9, verbose_name='Precion + IVA')),
                ('name_product', models.CharField(max_length=200, unique=True, verbose_name='Nombre del producto')),
                ('supplier', models.CharField(blank=True, max_length=200, null=True, verbose_name='Proveedor del producto')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orders_orderdetail_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order_detail_order', to='orders.order', verbose_name='Orden')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order_detail_product', to='products.product', verbose_name='Producto')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orders_orderdetail_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Última modificación por')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order_detail_user', to=settings.AUTH_USER_MODEL, verbose_name='Cliente')),
            ],
            options={
                'permissions': (('retrieve_orderdetail', 'Can retrieve orderdetail data'), ('list_orderdetail', 'Can list orderdetail data')),
            },
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha última de modificación')),
                ('is_active', models.BooleanField(default=True, verbose_name='Esta activo')),
                ('deleted', models.BooleanField(default=False, verbose_name='Eliminado')),
                ('payment', models.DecimalField(decimal_places=5, max_digits=9, verbose_name='Pago')),
                ('payment_method', models.CharField(blank=True, max_length=200, null=True, verbose_name='Metodo de pago')),
                ('residue', models.DecimalField(decimal_places=5, max_digits=9, verbose_name='Saldo')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orders_transactions_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transactions_order', to='orders.order', verbose_name='Orden')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orders_transactions_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Última modificación por')),
            ],
            options={
                'permissions': (('retrieve_transactions', 'Can retrieve transactions data'), ('list_transactions', 'Can list transactions data')),
            },
        ),
        migrations.CreateModel(
            name='TransactionsLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(max_length=100, verbose_name='Campo')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')),
                ('deleted', models.BooleanField(default=False, verbose_name='Eliminar')),
                ('before_char', models.CharField(blank=True, max_length=500, null=True, verbose_name='Texto antes')),
                ('after_char', models.CharField(blank=True, max_length=500, null=True, verbose_name='Texto después')),
                ('before_text', models.TextField(blank=True, null=True, verbose_name='Texto largo antes')),
                ('after_text', models.TextField(blank=True, null=True, verbose_name='Texto largo después')),
                ('before_id', models.IntegerField(blank=True, null=True, verbose_name='Id antes')),
                ('after_id', models.IntegerField(blank=True, null=True, verbose_name='Id después')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orders_transactionslog_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orders.transactions', verbose_name='Registro')),
            ],
            options={
                'permissions': (('retrieve_transactionslog', 'Can retrieve Transactionslog data'), ('list_transactionslog', 'Can list Transactionslog data')),
            },
        ),
        migrations.CreateModel(
            name='OrderLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(max_length=100, verbose_name='Campo')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')),
                ('deleted', models.BooleanField(default=False, verbose_name='Eliminar')),
                ('before_char', models.CharField(blank=True, max_length=500, null=True, verbose_name='Texto antes')),
                ('after_char', models.CharField(blank=True, max_length=500, null=True, verbose_name='Texto después')),
                ('before_text', models.TextField(blank=True, null=True, verbose_name='Texto largo antes')),
                ('after_text', models.TextField(blank=True, null=True, verbose_name='Texto largo después')),
                ('before_id', models.IntegerField(blank=True, null=True, verbose_name='Id antes')),
                ('after_id', models.IntegerField(blank=True, null=True, verbose_name='Id después')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orders_orderlog_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orders.order', verbose_name='Registro')),
            ],
            options={
                'permissions': (('retrieve_orderlog', 'Can retrieve Orderlog data'), ('list_orderlog', 'Can list Orderlog data')),
            },
        ),
        migrations.CreateModel(
            name='OrderDetailLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(max_length=100, verbose_name='Campo')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')),
                ('deleted', models.BooleanField(default=False, verbose_name='Eliminar')),
                ('before_char', models.CharField(blank=True, max_length=500, null=True, verbose_name='Texto antes')),
                ('after_char', models.CharField(blank=True, max_length=500, null=True, verbose_name='Texto después')),
                ('before_text', models.TextField(blank=True, null=True, verbose_name='Texto largo antes')),
                ('after_text', models.TextField(blank=True, null=True, verbose_name='Texto largo después')),
                ('before_id', models.IntegerField(blank=True, null=True, verbose_name='Id antes')),
                ('after_id', models.IntegerField(blank=True, null=True, verbose_name='Id después')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orders_orderdetaillog_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orders.orderdetail', verbose_name='Registro')),
            ],
            options={
                'permissions': (('retrieve_orderdetaillog', 'Can retrieve OrderDetaillog data'), ('list_orderdetaillog', 'Can list OrderDetaillog data')),
            },
        ),
    ]