from django.conf import settings
from django.db import models

from constants import NULLABLE


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='заголовок')
    body = models.TextField(verbose_name='содержимое')
    img = models.ImageField(upload_to='posts/', **NULLABLE, verbose_name='изображение')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    is_published = models.BooleanField(default=True, verbose_name='признак публикации')
    views = models.IntegerField(default=0, verbose_name='количество просмотров')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              **NULLABLE,
                              related_name='owner',
                              on_delete=models.SET_NULL,
                              verbose_name='создатель')

    def __str__(self):
        return f'{self.title} {self.body} {self.create_date} {self.views}'

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
        ordering = ('title',)
