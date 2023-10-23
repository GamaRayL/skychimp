# Generated by Django 4.2.6 on 2023-10-23 04:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='пользователь'),
        ),
        migrations.AddField(
            model_name='mailing',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.message', verbose_name='сообщение'),
        ),
        migrations.AddField(
            model_name='mailing',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='owner', to=settings.AUTH_USER_MODEL, verbose_name='создатель'),
        ),
        migrations.AddField(
            model_name='mailing',
            name='user',
            field=models.ManyToManyField(related_name='clients', to=settings.AUTH_USER_MODEL, verbose_name='клиенты'),
        ),
        migrations.AddField(
            model_name='log',
            name='mailing',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='logs', to='main.mailing', verbose_name='рассылка'),
        ),
    ]
