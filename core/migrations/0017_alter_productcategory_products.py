# Generated by Django 4.2.5 on 2024-03-25 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_alter_product_mixer_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='products',
            field=models.ManyToManyField(blank=True, default=None, to='core.product'),
        ),
    ]
