# Generated by Django 4.2.16 on 2024-11-20 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_max_limit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productoption',
            name='intr_rate',
            field=models.DecimalField(decimal_places=2, default=-1.0, max_digits=5, null=True),
        ),
    ]
