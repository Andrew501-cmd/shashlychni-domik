# Generated by Django 5.0.2 on 2024-02-18 22:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Заказчик'),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orders.orderstatus', verbose_name='Статус'),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orders.paymentmethod', verbose_name='Способ оплаты'),
        ),
        migrations.AddField(
            model_name='promotionalcode',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Владелец'),
        ),
        migrations.AddField(
            model_name='order',
            name='promotional_code',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='orders.promotionalcode', verbose_name='Промокод'),
        ),
        migrations.AddField(
            model_name='dish',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orders.section', verbose_name='Раздел'),
        ),
    ]
