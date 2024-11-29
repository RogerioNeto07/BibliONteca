from django.urls import path
from user import views

urlpatterns = [
<<<<<<< HEAD
    path('index', IndexReader),
    path('indexguest', IndexGuest),
    path('', Login), ]
=======
    path('home', views.home),
    path('', views.index),
    path('login', views.login),
    path('profile', views.Perfil),
    path('notifications', views.Notifications)]
>>>>>>> 8d746909c1cccaabcea4eb253fc2e321767b8349
