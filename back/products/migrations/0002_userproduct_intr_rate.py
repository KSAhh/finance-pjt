# Generated by Django 4.2.16 on 2024-11-25 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userproduct',
            name='intr_rate',
            field=models.DecimalField(decimal_places=2, default=-1.0, max_digits=5),
        ),
    ]
