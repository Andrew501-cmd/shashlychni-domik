# Generated by Django 5.0.2 on 2024-02-19 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_alter_order_promotional_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='anonymous',
        ),
    ]
