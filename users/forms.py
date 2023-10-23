from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms

from users.models import User


class StyleFormMixin:
    fields = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class LoginForm(StyleFormMixin, AuthenticationForm):
    class Meta:
        model = User
        fields = ('email', 'password')


class RegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class ProfileForm(StyleFormMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ('name', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()


class UpdateForm(StyleFormMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ('name', 'email', 'is_active')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()
        self.fields['is_active'].widget.attrs['class'] = 'form-check'
