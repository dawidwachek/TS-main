# Generated by Django 4.2.5 on 2024-01-08 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_rename_surveyresultitems_surveyresultitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderResult',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
