from django.db import models
from users.models import User
from django.conf import settings
from constants import NULLABLE, FREQUENCY_CHOOSE, MAILING_STATUS, LOG_STATUS


class Message(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class Mailing(models.Model):
    user = models.ManyToManyField(User, verbose_name='клиенты')
    send_time = models.DateTimeField(verbose_name='время рассылки')
    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOOSE, verbose_name='периодичность')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='сообщение')
    status = models.CharField(max_length=20, default='created', choices=MAILING_STATUS, verbose_name='статус')

    def __str__(self):
        return f'{self.get_frequency_display()} рассылка в {self.send_time}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'


class Log(models.Model):
    status = models.CharField(max_length=15, choices=LOG_STATUS, verbose_name='статус')
    server_response = models.BooleanField(default=False, verbose_name='ответ от сервера')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='дата и время последней попытки')
    mailing = models.ForeignKey(Mailing, on_delete=models.SET_NULL, **NULLABLE, related_name='logs',
                                verbose_name='рассылка')

    def __str__(self):
        return f'{self.mailing} - {self.status} ({self.timestamp})'

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'


class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    description = models.TextField(verbose_name='содержимое')
    image = models.ImageField(upload_to='posts/', **NULLABLE, verbose_name='изображение')
    views = models.IntegerField(default=0, verbose_name='просмотры')
    publish_date = models.DateTimeField(auto_now_add=True, verbose_name='дата публикации')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE,
                             verbose_name='пользователь')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
