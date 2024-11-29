from django.urls import path
from user import views

urlpatterns = [
    path('home', views.home),
    path('', views.index),
    path('login', views.login),
    path('profile', views.Perfil),
    path('notifications', views.Notifications)]