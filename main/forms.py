from django import forms

from main.models import Mailing


class DateInput(forms.DateTimeInput):
    input_type = 'datetime-local'


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class MailingForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Mailing

        exclude = ('status',)

        widgets = {
            'send_time': DateInput(),
        }
