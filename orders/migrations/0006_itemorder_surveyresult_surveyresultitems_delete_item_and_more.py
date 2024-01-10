# Generated by Django 4.2.5 on 2024-01-03 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_alter_question_question_type'),
        ('orders', '0005_remove_order_item_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemOrder',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='SurveyResult',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='SurveyResultItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_item', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.resultitem')),
                ('survey', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='orders.surveyresult')),
            ],
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.RemoveField(
            model_name='order',
            name='questionnaire_id',
        ),
        migrations.AddField(
            model_name='itemorder',
            name='order',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='orders.order'),
        ),
        migrations.AddField(
            model_name='itemorder',
            name='product',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.product'),
        ),
        migrations.AddField(
            model_name='itemorder',
            name='survey',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.questionnaire'),
        ),
        migrations.AddField(
            model_name='itemorder',
            name='survey_result',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='orders.surveyresult'),
        ),
    ]
