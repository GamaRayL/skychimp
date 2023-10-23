from django.urls import path
from django.views.decorators.cache import cache_page

from main.apps import MainConfig
from main.views import IndexView, MailingListView, MailingCreateView, MailingUpdateView, MailingDetailView, \
    MailingDeleteView, toggle_mailing_activation, LogListView

app_name = MainConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('logs/', cache_page(60)(LogListView.as_view()), name='logs'),
    path('mailings/', cache_page(60)(MailingListView.as_view()), name='mailings'),
    path('mailings/<int:pk>/', MailingDetailView.as_view(), name='mailing'),
    path('mailings/create/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailings/<int:pk>/update/', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailings/<int:pk>/delete/', MailingDeleteView.as_view(), name='mailing_delete'),
    path('mailings/toggle_mailing_activation/<int:pk>', toggle_mailing_activation, name='toggle_mailing_activation')
]