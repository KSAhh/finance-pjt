# Generated by Django 4.2.16 on 2024-11-21 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_alter_userproduct_product_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userproduct',
            name='etc_product',
        ),
        migrations.RemoveField(
            model_name='userproduct',
            name='status',
        ),
    ]
