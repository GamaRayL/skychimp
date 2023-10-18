from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from main.forms import MailingForm
from main.models import Mailing


class IndexView(TemplateView):
    template_name = 'main/home.html'


class MailingListView(ListView):
    model = Mailing

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Список рассылок'

        return context_data


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('main:mailings')


class MailingUpdateView(UpdateView):
    model = Mailing


class MailingDetailView(DetailView):
    model = Mailing

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        users_list = self.object.user.values_list('email', flat=True)
        context_data['users_list'] = users_list
        return context_data


class MailingDeleteView(DeleteView):
    model = Mailing
