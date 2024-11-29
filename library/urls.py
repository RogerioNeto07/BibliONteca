from django.urls import path
from library import views

urlpatterns = [
    path('home', views.home, name="libraryHome"),
]