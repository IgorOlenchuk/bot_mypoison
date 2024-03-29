from django.db import models
from django.utils import timezone


class TelegramUser(models.Model):

    id = models.IntegerField(unique=True, primary_key=True, verbose_name='ID')
    tg_name = models.CharField(max_length=30, verbose_name='Имя в телеграме')
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    is_banned = models.BooleanField(
        default=False, verbose_name='Заблокирован')
    is_push_maker = models.BooleanField(
        default=False, verbose_name='Создатель пуш сообщений')
    is_respondent = models.BooleanField(
        default=False, verbose_name='Администратор')
    reg_date = models.DateTimeField(default=timezone.now, verbose_name='Дата регистрации', db_index=True)

    class Meta:
        ordering = ["id"]
        verbose_name = 'пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.tg_name


class Settings(models.Model):

    id = models.IntegerField(unique=True, primary_key=True, verbose_name='ID')
    k_yuany = models.FloatField(null=True, blank=True, verbose_name='Коэф-т к курсы')
    k_comis_1 = models.IntegerField(null=True, blank=True, verbose_name='Коммиссия 1')
    k_comis_2 = models.IntegerField(null=True, blank=True, verbose_name='Коммиссия 2')
    
    class Meta:
        verbose_name = 'Настройки'

    def __int__(self):
        return self.id


class Order(models.Model):

    user = models.ForeignKey(
        TelegramUser,
        on_delete=models.CASCADE,
        related_name='models',
        verbose_name='Покупатель'
    )
    cost = models.CharField(max_length=150, null=True, blank=True, verbose_name='Стоимость за единицу в валюте')
    count = models.CharField(max_length=150, null=True, blank=True, verbose_name='Количество')
    size = models.CharField(max_length=150, null=True, blank=True, verbose_name='Размер')
    link = models.CharField(max_length=150, null=True, blank=True, verbose_name='Ссылка')
    total_cost = models.CharField(max_length=150, null=True, blank=True, verbose_name='Итоговая стоимость в руб.')
    order_date = models.DateTimeField(default=timezone.now, verbose_name='Дата заказа', db_index=True)
    
    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

    def __str__(self):
        return f'Дата заказа {self.order_date}'