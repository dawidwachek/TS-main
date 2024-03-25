# Generated by Django 4.2.5 on 2024-02-11 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('slug', models.CharField(blank=True, default=None, help_text='is autocomplete', max_length=100, null=True)),
                ('user', models.EmailField(max_length=100)),
            ],
        ),
    ]