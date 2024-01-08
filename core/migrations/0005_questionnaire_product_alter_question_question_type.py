# Generated by Django 4.2.5 on 2024-01-02 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_question_question_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnaire',
            name='product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='core.product'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('button', 'Button'), ('choice', 'Choice'), ('text', 'Text'), ('integer', 'Integer')], default='button', max_length=100),
        ),
    ]
