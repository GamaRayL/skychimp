from django.urls import path

from blog.apps import BlogConfig
from blog.views import PostListView
from django.views.decorators.cache import cache_page


app_name = BlogConfig.name

urlpatterns = [
    path('posts/', PostListView.as_view(), name='posts'),
]
