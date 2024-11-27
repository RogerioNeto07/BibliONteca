from django.urls import path
from user.views import IndexReader, IndexGuest, Login

urlpatterns = [
    path('index', IndexReader),
    path('indexguest', IndexGuest),
    path('', Login), ]