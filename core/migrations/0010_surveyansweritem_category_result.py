# Generated by Django 4.2.5 on 2024-02-15 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_remove_resultitem_category_resultitem_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='surveyansweritem',
            name='category_result',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.resultcategory'),
        ),
    ]
