# Generated by Django 3.2.4 on 2021-06-14 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210612_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='iva',
            field=models.DecimalField(decimal_places=5, max_digits=14, verbose_name='IVA'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=5, max_digits=14, verbose_name='Precio'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price_total',
            field=models.DecimalField(decimal_places=5, max_digits=14, verbose_name='Precion + IVA'),
        ),
    ]
