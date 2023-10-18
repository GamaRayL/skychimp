from django.urls import path

from main.apps import MainConfig
from main.views import IndexView, MailingListView, MailingCreateView, MailingUpdateView, MailingDetailView, MailingDeleteView

app_name = MainConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('mailings/', MailingListView.as_view(), name='mailings'),
    path('mailings/<int:pk>/', MailingDetailView.as_view(), name='mailing'),
    path('mailings/create/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailings/<int:pk>/update/', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailings/<int:pk>/delete/', MailingDeleteView.as_view(), name='mailing_delete'),
]