from django.urls import path
from user.views import TesteBase, Login

urlpatterns = [
    path('base', TesteBase),
    path('login', Login),
]
