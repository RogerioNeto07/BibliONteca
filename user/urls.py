from django.urls import path
from user import views

urlpatterns = [
    path('', views.Login), 
    path('home', views.home),
    path('', views.index),
    path('login', views.login),
    path('profile', views.Perfil),
    path('notifications', views.Notifications),
    path('pesquisa', views.Search),
    path('history', views.Bookhistory),
]


