from django.views.generic import ListView

from blog.models import Post


class PostListView(ListView):
    model = Post
    extra_context = {
        'title': 'Статьи'
    }



