# Generated by Django 3.2.4 on 2021-06-15 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_orderdetail_name_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='code_transactions',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Codigo de transacción'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, choices=[('PENDIENTE', 'PENDIENTE'), ('ABONADO', 'ABONADO'), ('PAGADO', 'PAGADO'), ('PAGADO - ENVIADO', 'PAGADO - ENVIADO'), ('PAGADO - ENTREGADO', 'PAGADO - ENTREGADO'), ('CANCELADO', 'CANCELADO'), ('FINALIZADO', 'FINALIZADO')], max_length=200, null=True, verbose_name='Estado'),
        ),
    ]
