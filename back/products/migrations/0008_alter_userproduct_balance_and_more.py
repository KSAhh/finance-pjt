# Generated by Django 4.2.16 on 2024-11-21 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_userproduct_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userproduct',
            name='balance',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
        migrations.AlterField(
            model_name='userproduct',
            name='product_type',
            field=models.CharField(choices=[('deposit', '예금'), ('saving', '저축'), ('etc', '기타')], default='etc', max_length=50),
        ),
    ]