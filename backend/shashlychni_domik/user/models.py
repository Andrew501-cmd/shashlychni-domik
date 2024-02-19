from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    phone = models.CharField(max_length=14, verbose_name='Номер телефона', null=True)
    quantity_orders = models.PositiveIntegerField(verbose_name='Количество заказов', null=True)
    wasted_money = models.PositiveBigIntegerField(verbose_name='Потрачено денег', null=True)
    isBaned = models.BooleanField(default = False, verbose_name='Забанен')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class SaveAddress(models.Model):
    user = models.ForeignKey(User, on_delete = models.PROTECT, verbose_name = 'Пользователь')
    city = models.CharField(max_length=255, verbose_name='Город', default='Москва')
    street = models.CharField(max_length=255, verbose_name='Улица')
    house = models.CharField(max_length=255, verbose_name='Дом')
    frame = models.CharField(max_length=255, verbose_name='Корпус', blank=True)
    structure = models.CharField(max_length=255, verbose_name='Строение', blank=True)
    floor = models.CharField(max_length=255, verbose_name='Этаж')
    apartment = models.CharField(max_length=255, verbose_name='Квартира')
    code = models.CharField(max_length=255, verbose_name='Код домофона', blank=True)

    class Meta:
        verbose_name = 'Сохраненный адрес'
        verbose_name_plural = 'Сохраненные адреса'