# Generated by Django 5.0.2 on 2024-04-09 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compra', '0003_alter_producto_options_alter_proveedor_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='dni',
            field=models.IntegerField(),
        ),
    ]
