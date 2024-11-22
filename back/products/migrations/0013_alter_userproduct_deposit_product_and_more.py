# Generated by Django 4.2.16 on 2024-11-21 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_alter_userproduct_etc_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userproduct',
            name='deposit_product',
            field=models.ForeignKey(blank=True, default='Unknown', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_products', to='products.depositproduct'),
        ),
        migrations.AlterField(
            model_name='userproduct',
            name='etc_product',
            field=models.CharField(blank=True, default='Unknown', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userproduct',
            name='saving_product',
            field=models.ForeignKey(blank=True, default='Unknown', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_products', to='products.savingproduct'),
        ),
    ]
