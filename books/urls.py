from django.urls import path
from books import views

app_name = 'books'

urlpatterns = [
    path('detalhe/', views.ViewDetailBook, name="detail-books"),
    path('feedback/', views.ViewFeedbackBook, name='feedback-book'),
    ]