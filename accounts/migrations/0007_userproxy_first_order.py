# Generated by Django 4.2.5 on 2023-10-02 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_userproxy_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='userproxy',
            name='first_order',
            field=models.BooleanField(default=True),
        ),
    ]
