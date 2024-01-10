# Generated by Django 4.2.5 on 2024-01-02 17:41

import core.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Exclusion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('name', models.CharField(max_length=100, validators=[core.models.validator_tag])),
                ('desription', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('tag', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=False)),
                ('product_type', models.CharField(choices=[('OPP', 'one product phisical'), ('OPO', 'one product online'), ('PPP', 'personalized product plus'), ('PPR', 'personalized product random')], default='PPR', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question_id', models.AutoField(primary_key=True, serialize=False)),
                ('question_name', models.CharField(max_length=50)),
                ('question_description', models.CharField(blank=True, max_length=255)),
                ('question', models.TextField(blank=True, default=None, null=True)),
                ('question_type', models.CharField(choices=[('choice', 'Choice'), ('integer', 'Integer'), ('button', 'Button'), ('text', 'Text')], default='button', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('slug', models.CharField(blank=True, max_length=101, null=True)),
                ('questionnaire_id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_email', models.EmailField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('training_id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.TextField(blank=True, null=True)),
                ('email_user', models.EmailField(blank=True, default=None, max_length=254, null=True)),
                ('email_creator', models.EmailField(blank=True, default=None, max_length=254, null=True)),
                ('public', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SurveyAnswerItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.answer')),
                ('question', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.question')),
                ('survey', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.questionnaire')),
            ],
        ),
        migrations.CreateModel(
            name='GoalItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.answer')),
                ('goal', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.goal')),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('exercise_id', models.AutoField(primary_key=True, serialize=False)),
                ('exercise_name', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, help_text='how do this exercise', null=True)),
                ('exercise_alert', models.TextField(blank=True, help_text='attenion to', null=True)),
                ('exercise_url', models.URLField(blank=True, help_text='link to video', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('training', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.training')),
            ],
        ),
        migrations.CreateModel(
            name='ExclusionItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.answer')),
                ('exlusion', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.exclusion')),
            ],
        ),
        migrations.CreateModel(
            name='AnswerItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.answer')),
                ('question', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.question')),
            ],
        ),
    ]
