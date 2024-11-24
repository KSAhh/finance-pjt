# Generated by Django 4.2.16 on 2024-11-24 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_alter_userproduct_end_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userproduct',
            name='duration_months',
            field=models.IntegerField(choices=[(1, '1개월'), (3, '3개월'), (6, '6개월'), (12, '12개월'), (24, '24개월'), (36, '36개월')], default=36),
        ),
        migrations.AlterField(
            model_name='userproduct',
            name='balance',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='userproduct',
            name='end_date',
            field=models.DateField(blank=True),
        ),
    ]
