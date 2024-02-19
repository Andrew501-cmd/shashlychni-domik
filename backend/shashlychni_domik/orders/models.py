from django.db import models
from user.models import User

# Create your models here.

class Section(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

class Dish(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя', unique=True)
    section = models.ForeignKey(Section, on_delete = models.PROTECT, verbose_name = 'Раздел')
    description = models.TextField(verbose_name='Описание', blank=True)
    image = models.ImageField(upload_to ='dishes/', verbose_name='Фото')
    count = models.PositiveIntegerField(verbose_name='Количество')
    price = models.PositiveIntegerField(verbose_name='Цена')
    weight = models.PositiveIntegerField(verbose_name='Вес')
    isActive = models.BooleanField(default = True, verbose_name='Активен')
    isBestseller = models.BooleanField(default = False, verbose_name='Хит продаж')
    isNew = models.BooleanField(default = False, verbose_name='Новый товар')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

class PaymentMethod(models.Model):
    method = models.CharField(max_length=255, verbose_name='Способ оплаты')

    def __str__(self):
        return self.method

    class Meta:
        verbose_name = 'Способ оплаты'
        verbose_name_plural = 'Способы оплаты'

class OrderStatus(models.Model):
    status = models.CharField(max_length=255, verbose_name='Статус')

    def __str__(self):
        return self.status
    
    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказа'

class PromotionalCode(models.Model):
    code = models.CharField(max_length=255, verbose_name='Промокод')
    user = models.ForeignKey(User, on_delete = models.PROTECT, verbose_name = 'Владелец', blank=True)
    discount = models.PositiveSmallIntegerField(verbose_name='Процент скидки')

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'Промокод'
        verbose_name_plural = 'Промокоды'

class Address(models.Model):
    city = models.CharField(max_length=255, verbose_name='Город', default='Москва')
    street = models.CharField(max_length=255, verbose_name='Улица')
    house = models.CharField(max_length=255, verbose_name='Дом')
    frame = models.CharField(max_length=255, verbose_name='Корпус', blank=True)
    structure = models.CharField(max_length=255, verbose_name='Строение', blank=True)
    floor = models.CharField(max_length=255, verbose_name='Этаж')
    apartment = models.CharField(max_length=255, verbose_name='Квартира')
    code = models.CharField(max_length=255, verbose_name='Код домофона', blank=True)

    def __str__(self):
        return 'Город ' + self.city + ', Ул. ' + self.street + ', Дом ' + self.house + ', Кв. ' + self.apartment

    class Meta:
        verbose_name = 'Адрес заказа'
        verbose_name_plural = 'Адреса заказов'

class Order(models.Model):
    #anonymous = models.BooleanField(verbose_name='Аноним')
    user = models.ForeignKey(User, on_delete = models.PROTECT, verbose_name = 'Заказчик', blank=True, null=True)
    name = models.CharField(max_length=255, verbose_name='Имя', blank=True)
    surname = models.CharField(max_length=255, verbose_name='Фамилия', blank=True)
    patronymic = models.CharField(max_length=255, verbose_name='Отчество', blank=True)
    phone = models.CharField(max_length=14, verbose_name='Номер телефона', blank=True)
    email = models.EmailField(verbose_name='Почта', blank=True)
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    address = models.OneToOneField(Address, on_delete = models.PROTECT, verbose_name='Адрес')
    date_delivery = models.DateTimeField(verbose_name='Время доставки', blank=True, null=True)
    payment_method = models.ForeignKey(PaymentMethod, on_delete = models.PROTECT, verbose_name = 'Способ оплаты')
    status = models.ForeignKey(OrderStatus, on_delete = models.PROTECT, verbose_name = 'Статус')
    promotional_code = models.ForeignKey(PromotionalCode, on_delete = models.PROTECT, verbose_name = 'Промокод', blank=True, null=True)
    cutlery = models.PositiveSmallIntegerField(verbose_name='Количество столовых приборов')
    comment = models.TextField(verbose_name = 'Комментарий', blank=True)
    menu = models.ManyToManyField(Dish, verbose_name='Заказ')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'