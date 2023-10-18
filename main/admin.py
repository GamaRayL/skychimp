from django.contrib import admin

from main.models import Mailing, Message, Post


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('send_time', 'message', 'status', 'frequency',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'views', 'publish_date', 'user',)