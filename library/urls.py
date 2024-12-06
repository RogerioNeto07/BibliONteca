from django.urls import path
from library import views

urlpatterns = [
    path('paginaInicial', views.home, name="home"),
    path('cadastrarUsuario', views.register, name="registerUser"),
    path('cadastrarLivro', views.registerBook, name="regirterBook"),
    path('emprestarLivro', views.loanBook, name="loanBook"),
    path('devolverLivro', views.returnBook, name="returnBook"),
    path('renovarLivro', views.renewBook, name="renewBook"),
    path('listarLivros', views.listBooks, name="listBooks"),
    path('listarUsuarios', views.listUser, name="listUser"),
    path('pendenciasUsuarios', views.pendenceUser, name="pendenceUser"),
]