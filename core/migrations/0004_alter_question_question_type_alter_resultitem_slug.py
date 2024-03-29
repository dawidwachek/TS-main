# Generated by Django 4.2.5 on 2024-02-11 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_surveyresultcategoryitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(blank=True, choices=[('text', 'Text - not active now'), ('button', 'One choice'), ('choice', 'More Choice'), ('integer', 'Value'), ('category', 'Category Choice')], default='button', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='resultitem',
            name='slug',
            field=models.CharField(blank=True, default=None, help_text='is autocomplete', max_length=100, null=True),
        ),
    ]
