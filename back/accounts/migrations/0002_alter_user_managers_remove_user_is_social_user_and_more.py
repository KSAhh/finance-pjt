# Generated by Django 4.2.16 on 2024-11-17 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_social_user',
        ),
        migrations.RemoveField(
            model_name='user',
            name='social_login_provider',
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateField(auto_now_add=True),
        ),
    ]
