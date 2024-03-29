# Generated by Django 4.2.5 on 2024-02-06 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('banner_id', models.AutoField(primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=False)),
                ('has_link', models.BooleanField(default=False)),
                ('link', models.CharField(default=None, max_length=1000, null=True)),
                ('text', models.CharField(default=None, max_length=255, null=True)),
                ('start_at', models.DateField(blank=True, default=None, null=True)),
                ('end_at', models.DateField(blank=True, default=None, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('coupon_id', models.AutoField(primary_key=True, serialize=False)),
                ('coupon_name', models.CharField(max_length=255, unique=True)),
                ('is_active', models.BooleanField(default=False)),
                ('zero_amount', models.BooleanField(default=False, help_text='coupon resetting the amount')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('uses_coupon', models.DecimalField(decimal_places=0, default=0, max_digits=4)),
                ('max_uses_coupon', models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True)),
                ('value_coupon', models.DecimalField(decimal_places=2, default=0, help_text='amount or percentage', max_digits=5)),
                ('type_coupon', models.CharField(choices=[('PE', 'percent'), ('AM', 'amount')], max_length=255, null=True)),
                ('assigment', models.BooleanField(default=False)),
                ('email_assignment', models.EmailField(blank=True, default=None, max_length=254, null=True)),
                ('max_value_coupon', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('start_date_use', models.DateField(blank=True, default=None, null=True)),
                ('end_date_use', models.DateField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reflink',
            fields=[
                ('reflink_id', models.AutoField(primary_key=True, serialize=False)),
                ('name_user', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('uses_reflink', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('link_reflink', models.TextField(default='your reflink is domain + reflink/ + id reflinkworking at this :)')),
            ],
        ),
    ]
