from django.db import models
from constants import NULLABLE

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Модель представляет пользователя в системе"""
    username = None

    email = models.EmailField(unique=True, verbose_name='почта')
    comment = models.TextField(**NULLABLE, verbose_name='комментарий')
    first_name = models.CharField(max_length=50, **NULLABLE, verbose_name='имя')
    last_name = models.CharField(max_length=50, **NULLABLE, verbose_name='фамилия')
    middle_name = models.CharField(max_length=50, **NULLABLE, verbose_name='отчество')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
