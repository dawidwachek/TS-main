# Generated by Django 4.2.5 on 2024-03-24 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_historicalorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalorder',
            name='paid_at',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='paid_at',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
