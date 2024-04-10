# Generated by Django 5.0.2 on 2024-04-09 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compra', '0002_producto_proveedor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producto',
            options={'ordering': ['nombre', '-stock_actual'], 'verbose_name_plural': 'Productos'},
        ),
        migrations.AlterModelOptions(
            name='proveedor',
            options={'ordering': ['id', 'apellido', 'nombre'], 'verbose_name_plural': 'Proveedores'},
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='dni',
            field=models.IntegerField(max_length=9),
        ),
    ]
