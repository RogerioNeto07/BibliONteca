from django.urls import path
from user import views

urlpatterns = [
    path('index', views.IndexReader),
    path('indexguest', views.IndexGuest),
    path('', views.Login), 
    path('home', views.home),
    path('', views.index),
    path('login', views.login),
    path('profile', views.Perfil),
    path('notifications', views.Notifications)]
