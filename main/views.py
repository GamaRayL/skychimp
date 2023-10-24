from main.forms import MailingForm
from django.shortcuts import redirect
from constants import MAILING_CREATED
from main.models import Mailing, Post, Log
from django.urls import reverse_lazy, reverse
from django.views.decorators.cache import cache_page
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, CreateView, DetailView, DeleteView, UpdateView, ListView


class IndexView(TemplateView):
    template_name = 'main/home.html'
    cache_page(60)

    def get_context_data(self, **kwargs):
        random_blog_posts = Post.objects.order_by('?')[:3]
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Главная страница'
        context_data['total_mailings'] = Mailing.objects.count()
        context_data['active_mailings'] = Mailing.objects.filter(status=MAILING_CREATED).count()
        context_data['unique_clients'] = Mailing.objects.values('user').distinct().count()
        context_data['random_blog_posts'] = random_blog_posts

        return context_data


class MailingListView(LoginRequiredMixin, ListView):
    model = Mailing

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Список рассылок'

        return context_data


class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('main:mailings')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    form_class = MailingForm

    def get_success_url(self):
        return reverse('main:mailing', args=[self.object.pk])


class MailingDetailView(LoginRequiredMixin, DetailView):
    model = Mailing

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        users_list = self.object.user.values_list('email', flat=True)
        context_data['title'] = 'Текущая рассылка'
        context_data['users_list'] = users_list

        if self.object.owner == self.request.user:
            context_data['true_user'] = True

        return context_data


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailing
    success_url = reverse_lazy('main:mailings')
    extra_context = {
        'title': 'Удаление рассылки'
    }


class LogListView(ListView):
    model = Log
    extra_context = {
        'title': 'Логи рассылок'
    }


@login_required
def toggle_mailing_activation(request, pk):
    mailing = Mailing.objects.get(pk=pk)
    if mailing.is_active:
        mailing.is_active = False
    else:
        mailing.is_active = True

    mailing.save()
    return redirect(reverse('main:mailings'))
