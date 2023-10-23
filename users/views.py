import random

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from users.forms import LoginForm, RegisterForm, ProfileForm, UpdateForm
from users.models import User


class LoginView(BaseLoginView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('main:home')


class RegisterView(CreateView):
    model = User
    template_name = 'users/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        key = str(random.randint(1, 99999))
        form.instance.key = key
        user = form.save()

        verify_email_url = reverse('users:verify_email', args=[key])

        send_mail(
            subject='Поздравляем с регистрацией',
            message=f'Вы зарегистрировались на нашей платформе. '
                    f'Для продолжения регистрации перейдите по ссылке '
                    f'{get_current_site(self.request)}{verify_email_url}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email]
        )

        return super().form_valid(form)


def verify_email(request, key):
    user = User.objects.get(key=key)

    if not user.is_active:
        user.is_active = True
        user.save()
        return HttpResponse("Email успешно подтвержден!")
    else:
        return HttpResponse("Email уже подтвержден!")


class UserListView(ListView):
    model = User

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Список пользователей'

        return context_data


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Пользователь'

        return context_data


class UserUpdateView(UpdateView):
    model = User
    form_class = UpdateForm
    success_url = reverse_lazy('users:user_list')


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy('main:home')

    def get_object(self, queryset=None):
        return self.request.user


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy('users:user_list')
    extra_context = {
        'title': 'Удаление пользователя'
    }


@login_required
def toggle_user_activation(request, pk):
    user = User.objects.get(pk=pk)
    if user.is_active:
        user.is_active = False
    else:
        user.is_active = True

    user.save()
    return redirect(reverse('users:user_list'))
