# Generated by Django 4.2.5 on 2024-01-15 18:11

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('settings', '__first__'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superadmin', models.BooleanField(default=False)),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Permissions',
            fields=[
                ('permission_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.permission')),
            ],
            options={
                'permissions': [('can_do_something', 'Can do something special')],
            },
            bases=('auth.permission',),
            managers=[
                ('objects', django.contrib.auth.models.PermissionManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserProxy',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=15, null=True)),
                ('last_name', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('phone_number', models.DecimalField(blank=True, decimal_places=0, default='123456789', max_digits=9, null=True)),
                ('date_birthday', models.DateField(blank=True, null=True)),
                ('first_step', models.BooleanField(default=True)),
                ('first_order', models.BooleanField(default=True)),
                ('regulations', models.BooleanField(default=False)),
                ('active_sub', models.BooleanField(default=False)),
                ('id_sub', models.DecimalField(blank=True, decimal_places=0, max_digits=7, null=True)),
                ('price_base', models.DecimalField(decimal_places=2, max_digits=7, null=True)),
                ('regulations_id', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='settings.regulation')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerAdress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('post_code', models.CharField(blank=True, default=None, max_length=7, null=True)),
                ('adress_line_1', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('adress_line_2', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('country', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('adress_type', models.CharField(choices=[('BI', 'billing'), ('DE', 'delivery')], default='BI', max_length=100)),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Customer Adress',
            },
        ),
    ]
