# Generated by Django 3.2.4 on 2021-06-14 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='iva',
            field=models.DecimalField(decimal_places=5, max_digits=14, verbose_name='IVA'),
        ),
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.DecimalField(decimal_places=5, max_digits=14, verbose_name='Precio'),
        ),
        migrations.AlterField(
            model_name='order',
            name='price_total',
            field=models.DecimalField(decimal_places=5, max_digits=14, verbose_name='Precion + IVA'),
        ),
        migrations.AlterField(
            model_name='order',
            name='residue',
            field=models.DecimalField(decimal_places=5, max_digits=14, verbose_name='Saldo'),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='iva',
            field=models.DecimalField(decimal_places=5, max_digits=14, verbose_name='IVA'),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='price',
            field=models.DecimalField(decimal_places=5, max_digits=14, verbose_name='Precio'),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='price_total',
            field=models.DecimalField(decimal_places=5, max_digits=14, verbose_name='Precion + IVA'),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='payment',
            field=models.DecimalField(decimal_places=5, max_digits=14, verbose_name='Pago'),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='residue',
            field=models.DecimalField(decimal_places=5, max_digits=14, verbose_name='Saldo'),
        ),
    ]
