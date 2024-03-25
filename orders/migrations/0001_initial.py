# Generated by Django 4.2.5 on 2024-02-25 12:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0013_remove_surveyansweritem_category_result'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderResult',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('survey', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.questionnaire')),
            ],
        ),
        migrations.CreateModel(
            name='SurveyResult',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('survey', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.questionnaire')),
            ],
        ),
        migrations.CreateModel(
            name='SurveyResultItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_item', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.resultitem')),
                ('survey', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='orders.surveyresult')),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('sub_id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderResultItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_result', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='orders.orderresult')),
                ('result_category', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.resultcategory')),
                ('result_item', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.resultitem')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_status', models.CharField(choices=[('OC', 'Order Created'), ('WP', 'Waiting for Payment'), ('PA', 'Payment Accepted'), ('PE', 'Payment Error'), ('WA', 'Waiting for Acception'), ('PRE', 'Personalizations Error'), ('OA', 'Order Accepted'), ('OS', 'Order Sended'), ('OCA', 'Order Cancelled'), ('OR', 'Order Refounded')], default='OC', max_length=255)),
                ('user_name', models.CharField(blank=True, max_length=30)),
                ('language', models.CharField(choices=[('PL', 'Polish'), ('EN', 'English')], default='EN', max_length=255)),
                ('order_error', models.CharField(blank=True, max_length=255, null=True)),
                ('name_coupon', models.CharField(blank=True, max_length=15, null=True)),
                ('original_price', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=7, null=True)),
                ('pay_price', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=7, null=True)),
                ('editor_email', models.EmailField(blank=True, max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('visible', models.BooleanField(default=True)),
                ('email_adress', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ItemOrder',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=7, null=True)),
                ('order', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='orders.order')),
                ('order_result', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='orders.orderresult')),
                ('product', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.product')),
                ('survey', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.questionnaire')),
                ('survey_result', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='orders.surveyresult')),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
