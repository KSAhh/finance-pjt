# Generated by Django 4.2.16 on 2024-11-19 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='join_way',
            field=models.CharField(default='-', max_length=255),
        ),
    ]
