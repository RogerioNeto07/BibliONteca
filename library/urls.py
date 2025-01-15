from django.urls import path
from library import views


urlpatterns = [
    path('pagina-inicial/', views.home, name="home-lib"),
    path('cadastrar-usuario/', views.register, name="registerUser"),
    path('cadastrar-livro/', views.registerBook, name="regirterBook"),
    path('emprestar-livro/', views.loanBook, name="loanBook"),
    path('devolver-livro/', views.returnBook, name="returnBook"),
    path('renovar-livro/', views.renewBook, name="renewBook"),
    path('listar-livros/', views.listBooks, name="listBooks"),
    path('listar-usuarios/', views.listUser, name="listUser"),
    path('pendencias-usuarios/', views.pendenceUser, name="pendenceUser"),
    path('todos-emprestimos/', views.allLoans, name="allLoans"),
    path('emprestimos-pendentes/', views.pendencesBook, name="pendencesBook"),
    path('detalhes-pendencias-usuarios/', views.detailsPendencesUser, name="detailsPendencesUser"),
    path('detalhes-pendencias-livros/', views.detailsPendencesBook, name="detailsPendencesBook"),
    path('perfil/', views.profile, name='profile'),
]
