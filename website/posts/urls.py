from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
    path('group/<slug:slug>/', views.group_post, name='group_post')

]
