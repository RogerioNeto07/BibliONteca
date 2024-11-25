from django.urls import path
from user.views import TesteBase

urlpatterns = [
    path('base', TesteBase),
]
