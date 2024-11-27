from django.urls import path
from user.views import IndexReader, IndexGuest, Login, Perfil

urlpatterns = [
    path('index', IndexReader),
    path('indexguest', IndexGuest),
    path('', Login), 
    path('perfil', Perfil),
    ]