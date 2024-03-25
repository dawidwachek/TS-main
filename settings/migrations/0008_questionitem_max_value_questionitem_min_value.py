# Generated by Django 4.2.5 on 2024-03-18 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0007_remove_questionitem_min_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionitem',
            name='max_value',
            field=models.CharField(blank=True, default=None, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='questionitem',
            name='min_value',
            field=models.CharField(blank=True, default=None, max_length=5, null=True),
        ),
    ]
