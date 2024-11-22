# Generated by Django 4.2.16 on 2024-11-21 04:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='DepositProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kor_co_nm', models.CharField(default='Unknown', max_length=255)),
                ('fin_prdt_cd', models.CharField(default='Unknown', max_length=255)),
                ('fin_prdt_nm', models.CharField(default='Unknown', max_length=255)),
                ('join_way', models.CharField(default='Unknown', max_length=255)),
                ('mtrt_int', models.TextField(default='Unknown')),
                ('spcl_cnd', models.TextField(default='Unknown')),
                ('join_deny', models.IntegerField(default=1)),
                ('join_member', models.TextField(default='실명의 개인')),
                ('etc_note', models.TextField(default='Unknown')),
                ('fin_co_subm_day', models.CharField(default='000000000000', max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='SavingProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kor_co_nm', models.CharField(default='Unknown', max_length=255)),
                ('fin_prdt_cd', models.CharField(default='Unknown', max_length=255)),
                ('fin_prdt_nm', models.CharField(default='Unknown', max_length=255)),
                ('join_way', models.CharField(default='Unknown', max_length=255)),
                ('mtrt_int', models.TextField(default='Unknown')),
                ('spcl_cnd', models.TextField(default='Unknown')),
                ('join_deny', models.IntegerField(default=1)),
                ('join_member', models.TextField(default='실명의 개인')),
                ('etc_note', models.TextField(default='Unknown')),
                ('fin_co_subm_day', models.CharField(default='000000000000', max_length=12)),
                ('max_limit', models.DecimalField(decimal_places=2, default=-1.0, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='ProductOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('intr_rate_type_nm', models.CharField(default='Unknown', max_length=100)),
                ('save_trm', models.IntegerField(default=-1)),
                ('intr_rate', models.DecimalField(decimal_places=2, default=-1.0, max_digits=5)),
                ('intr_rate2', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('rsrv_type_nm', models.CharField(default='Unknown', max_length=100)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
        ),
    ]
