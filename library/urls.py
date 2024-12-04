from django.urls import path
from library import views

urlpatterns = [
    path('home', views.home, name="home"),
    path('register', views.register, name="cadastrarUsuario"),
    path('register/book', views.registerBook, name="cadastrarLivro"),
    path('loan/book', views.loanBook, name="emprestarLivro"),
    path('return/book', views.returnBook, name="devolverLivro"),
]