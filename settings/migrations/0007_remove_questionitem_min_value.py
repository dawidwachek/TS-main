# Generated by Django 4.2.5 on 2024-03-18 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0006_questionitem_min_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionitem',
            name='min_value',
        ),
    ]