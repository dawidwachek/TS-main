# Generated by Django 4.2.5 on 2024-03-18 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0005_alter_questionitem_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionitem',
            name='min_value',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]