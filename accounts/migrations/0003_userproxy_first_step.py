# Generated by Django 4.2.1 on 2023-09-04 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='userproxy',
            name='first_step',
            field=models.BooleanField(default=True),
        ),
    ]
