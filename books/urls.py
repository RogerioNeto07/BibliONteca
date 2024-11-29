from django.urls import path
from books import views

urlpatterns = [
    path('detalhe/', views.ViewDetailBook, name="detail-books"),
    ]