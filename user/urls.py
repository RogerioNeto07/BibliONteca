from django.urls import path
from user.views import *

urlpatterns = [
    path('index', IndexReader),
    path('indexguest', IndexGuest),
    path('', Login), 
    path('profile', Perfil),
    path('notifications', Notifications),
    ]