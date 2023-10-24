from django.urls import path
from users.apps import UsersConfig
from django.contrib.auth.views import LogoutView
from users.views import LoginView, RegisterView, verify_email, UserListView, UserDetailView, ProfileView, \
    UserUpdateView, toggle_user_activation, UserDeleteView

app_name = UsersConfig.name

urlpatterns = [
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('users/login/', LoginView.as_view(), name='login'),
    path('users/update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('users/profile/', ProfileView.as_view(), name='profile'),
    path('users/logout/', LogoutView.as_view(), name='logout'),
    path('users/regiseter/', RegisterView.as_view(), name='register'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
    path('users/verify_email/<int:key>/', verify_email, name='verify_email'),
    path('users/toggle_user_activation/<int:pk>/', toggle_user_activation, name='toggle_user_activation')
]