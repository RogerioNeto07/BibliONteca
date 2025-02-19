from django.urls import path
from books import views

app_name = 'books'

urlpatterns = [
    path('detalhe-livro/', views.ViewDetailBook.as_view(), name="detail-books"),
    path('feedback-livro/', views.ViewFeedbackBook.as_view(), name='feedback-book'),
]
