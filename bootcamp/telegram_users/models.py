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
