# Generated by Django 4.2.5 on 2024-01-08 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0059_alter_question_question_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('text', 'Text'), ('choice', 'Choice'), ('button', 'Button'), ('integer', 'Integer')], default='button', max_length=100),
        ),
    ]