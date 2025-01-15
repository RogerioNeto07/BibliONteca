from django.urls import path
from user import views

urlpatterns = [
    path('', views.Login), 
    path('home', views.home, name='home'),
    path('', views.index),
    path('login', views.login, name='login'),
    path('profile', views.Perfil, name='profile-user'),
    path('notifications', views.Notifications, name='notifications'),
    path('pesquisa', views.Search, name='pesquisa'),
    path('history', views.Bookhistory, name='history'),
]


