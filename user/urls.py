from django.urls import path
from user.views import IndexReader, IndexGuest, Login

urlpatterns = [
<<<<<<< Updated upstream
    path('index', IndexReader),
    path('indexguest', IndexGuest),
    path('', Login), ]
=======
    path('home', views.home),
    path('', views.index),
    path('login', views.login), 
]

>>>>>>> Stashed changes
