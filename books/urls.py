from django.urls import path
from books import views

app_name = 'books'

urlpatterns = [
    path('detalhe-livro/<int:id>/', views.ViewDetailBook, name="detail-books"),
    path('feedback-livro/', views.ViewFeedbackBook, name='feedback-book'),
]
