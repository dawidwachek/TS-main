# Generated by Django 4.2.5 on 2023-09-28 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_exclussion_maximum_repeat_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='exclussion',
            name='maximum_load',
            field=models.DecimalField(blank=True, decimal_places=0, default=None, max_digits=4),
        ),
        migrations.AddField(
            model_name='exclussion',
            name='minimum_load',
            field=models.DecimalField(blank=True, decimal_places=0, default=None, max_digits=4),
        ),
        migrations.AddField(
            model_name='exclussion',
            name='url_link',
            field=models.CharField(blank=True, default=None, max_length=1000),
        ),
    ]
