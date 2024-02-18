# Generated by Django 5.0.2 on 2024-02-18 20:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
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
                ('code', models.CharField(max_length=255, verbose_name='Код домофона')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Сохраненный адрес',
                'verbose_name_plural': 'Сохраненные адреса',
            },
        ),
    ]