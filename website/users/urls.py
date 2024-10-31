from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import PasswordChangeDoneView
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetCompleteView
from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('signup/', views.SignUp.as_view(),
         name='signup'),
    # Логин.
    path(
        'login/',
        LoginView.as_view(),
        name='login'
    ),
    # Логаут.
    path('logout/', LogoutView.as_view(),
         name='logout'),
    # Изменение пароля.
    path('password_change/', PasswordChangeView.as_view(),
         name='password_change'),
    # Сообщение об успешном изменении пароля.
    path('password_change/done/', PasswordChangeDoneView.as_view(),
         name='password_change_done'),
    # Восстановление пароля.
    path('password_reset/', PasswordResetView.as_view(),
         name='password_reset'),
    # Сообщение об отправке ссылки для восстановления пароля.
    path('password_reset/done/', PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    # Вход по ссылке для восстановления пароля.
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    # Сообщение об успешном восстановлении пароля.
    path('reset/done/', PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
]
