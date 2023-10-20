from django.views.generic import TemplateView, CreateView, DetailView, DeleteView, UpdateView, ListView
from django.urls import reverse_lazy, reverse
from main.forms import MailingForm
from main.models import Mailing
from main.services import send_mailing


class IndexView(TemplateView):
    template_name = 'main/home.html'
    extra_context = {
        'title': 'Главная страница'
    }


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
    form_class = MailingForm

    def get_success_url(self):
        return reverse('main:mailing', args=[self.object.pk])


class MailingDetailView(DetailView):
    model = Mailing

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        users_list = self.object.user.values_list('email', flat=True)
        context_data['title'] = 'Текущая рассылка'
        context_data['users_list'] = users_list
        print(send_mailing())
        return context_data


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('main:mailings')
