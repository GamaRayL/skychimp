from django.db import models
from constants import frequency_choose, mailing_status, log_status, NULLABLE


class Mailing(models.Model):
    send_time = models.DateTimeField(verbose_name='время рассылки')
    status = models.CharField(max_length=20, choices=mailing_status, verbose_name='статус')
    frequency = models.CharField(max_length=10, choices=frequency_choose, verbose_name='периодичность')

    def __str__(self):
        return f'{self.get_frequency_display()} рассылка в {self.send_time}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'


class Message(models.Model):
    description = models.TextField(verbose_name='описание')
    title = models.CharField(max_length=150, verbose_name='заголовок')
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='рассылка')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class Log(models.Model):
    server_response = models.CharField
    status = models.CharField(max_length=15, choices=log_status, verbose_name='статус')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='дата и время последней попытки')
    mailing = models.ForeignKey(Mailing, on_delete=models.SET_NULL, **NULLABLE, default='-', verbose_name='рассылка')

    def __str__(self):
        return f'{self.mailing} - {self.status} ({self.timestamp})'

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'


class Post(models.Model):
    description = models.TextField(verbose_name='содержимое')
    views = models.IntegerField(default=0, verbose_name='просмотры')
    title = models.CharField(max_length=150, verbose_name='заголовок')
    image = models.ImageField(upload_to='posts/', **NULLABLE, verbose_name='изображение')
    publish_date = models.DateTimeField(auto_now_add=True, verbose_name='дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
