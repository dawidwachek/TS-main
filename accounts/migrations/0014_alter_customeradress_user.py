# Generated by Django 4.2.5 on 2024-02-08 17:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_alter_user_user_permissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeradress',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
