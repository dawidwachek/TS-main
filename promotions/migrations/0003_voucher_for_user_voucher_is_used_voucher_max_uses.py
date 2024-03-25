# Generated by Django 4.2.5 on 2024-02-11 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotions', '0002_voucher'),
    ]

    operations = [
        migrations.AddField(
            model_name='voucher',
            name='for_user',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='voucher',
            name='is_used',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='voucher',
            name='max_uses',
            field=models.IntegerField(default=1),
        ),
    ]