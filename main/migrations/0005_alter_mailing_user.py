# Generated by Django 4.2.6 on 2023-10-20 05:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0004_alter_mailing_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='клиенты'),
        ),
    ]
