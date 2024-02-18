# Generated by Django 5.0.2 on 2024-02-18 22:18

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrimaryGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('isEdit', models.BooleanField(default=False, verbose_name='Права на редактирование')),
            ],
            options={
                'verbose_name': 'Роль',
                'verbose_name_plural': 'Роли',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Имя')),
                ('surname', models.CharField(max_length=255, null=True, verbose_name='Фамилия')),
                ('patronymic', models.CharField(blank=True, max_length=255, verbose_name='Отчество')),
                ('phone', models.CharField(max_length=14, null=True, verbose_name='Номер телефона')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')),
                ('quantity_orders', models.PositiveIntegerField(null=True, verbose_name='Количество заказов')),
                ('wasted_money', models.PositiveBigIntegerField(null=True, verbose_name='Потрачено денег')),
                ('isBaned', models.BooleanField(default=False, verbose_name='Забанен')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('primary', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='user.primarygroup', verbose_name='Роль')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='SaveAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(default='Москва', max_length=255, verbose_name='Город')),
                ('street', models.CharField(max_length=255, verbose_name='Улица')),
                ('house', models.CharField(max_length=255, verbose_name='Дом')),
                ('frame', models.CharField(blank=True, max_length=255, verbose_name='Корпус')),
                ('structure', models.CharField(blank=True, max_length=255, verbose_name='Строение')),
                ('floor', models.CharField(max_length=255, verbose_name='Этаж')),
                ('apartment', models.CharField(max_length=255, verbose_name='Квартира')),
                ('code', models.CharField(blank=True, max_length=255, verbose_name='Код домофона')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Сохраненный адрес',
                'verbose_name_plural': 'Сохраненные адреса',
            },
        ),
    ]
