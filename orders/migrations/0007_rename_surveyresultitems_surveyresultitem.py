# Generated by Django 4.2.5 on 2024-01-03 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0044_alter_question_question_type'),
        ('orders', '0006_itemorder_surveyresult_surveyresultitems_delete_item_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SurveyResultItems',
            new_name='SurveyResultItem',
        ),
    ]
