from django.contrib import admin

from main.models import Mailing, Message, Post, Log


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('time', 'date_run', 'message', 'status', 'frequency',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('status', 'mailing', 'timestamp', 'server_response')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'views', 'publish_date', 'user',)
