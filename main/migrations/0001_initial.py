# Generated by Django 4.2.6 on 2023-10-18 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('success', 'Успешно'), ('failure', 'Неуспешно')], max_length=15, verbose_name='статус')),
                ('server_response', models.BooleanField(default=False, verbose_name='ответ от сервера')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='дата и время последней попытки')),
            ],
            options={
                'verbose_name': 'лог',
                'verbose_name_plural': 'логи',
            },
        ),
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('send_time', models.DateTimeField(verbose_name='время рассылки')),
                ('status', models.CharField(choices=[('created', 'Создана'), ('started', 'Запущена'), ('closed', 'Завершена')], max_length=20, verbose_name='статус')),
                ('frequency', models.CharField(choices=[('daily', 'Раз в день'), ('weekly', 'Раз в неделю'), ('monthly', 'Раз в месяц')], max_length=10, verbose_name='периодичность')),
            ],
            options={
                'verbose_name': 'рассылка',
                'verbose_name_plural': 'рассылки',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='описание')),
                ('title', models.CharField(max_length=150, verbose_name='заголовок')),
            ],
            options={
                'verbose_name': 'сообщение',
                'verbose_name_plural': 'сообщения',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='содержимое')),
                ('views', models.IntegerField(default=0, verbose_name='просмотры')),
                ('title', models.CharField(max_length=150, verbose_name='заголовок')),
                ('image', models.ImageField(blank=True, null=True, upload_to='posts/', verbose_name='изображение')),
                ('publish_date', models.DateTimeField(auto_now_add=True, verbose_name='дата публикации')),
            ],
            options={
                'verbose_name': 'пост',
                'verbose_name_plural': 'посты',
            },
        ),
    ]