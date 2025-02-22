from django.urls import path
from library import views

app_name = 'library'

urlpatterns = [
    path('pagina-inicial/', views.HomeView.as_view(), name="home-lib"),
    path('detalhe-livro/<int:pk>', views.ViewDetailBook, name="detail-books"),
    path('feedback-livro/<int:pk>', views.ViewFeedbackBook, name='feedback-book'),
    path('adicionar-comentario/<int:pk>', views.ViewComentarios, name="comments-book"),
    path('cadastrar-usuario/', views.RegisterView.as_view(), name="registerUser"),
    path('cadastrar-livro/', views.RegisterBookView.as_view(), name="registerBook"),
    path('emprestar-livro/', views.LoanBookView.as_view(), name="loanBook"),
    path('devolver-livro/', views.ReturnBookView.as_view(), name="returnBook"),
    path('renovar-livro/', views.RenewBookView.as_view(), name="renewBook"),
    path('listar-livros/', views.ListBooksView.as_view(), name="listBooks"),
    path('listar-usuarios/', views.ListUserView.as_view(), name="listUser"),
    path('pendencias-usuarios/', views.PendenceUserView.as_view(), name="pendenceUser"),
    path('todos-emprestimos/', views.AllLoansView.as_view(), name="allLoans"),
    path('perfil/<int:usuario_id>/', views.PerfilUsuarioView.as_view(), name='perfil_usuario'),
    path('emprestimos-pendentes/', views.PendencesBookView.as_view(), name="pendencesBook"),
    path('detalhes-pendencias-usuarios/', views.DetailsPendencesUserView.as_view(), name="detailsPendencesUser"),
    path('detalhes-pendencias-livros/', views.DetailsPendencesBookView.as_view(), name="detailsPendencesBook"),
    path('perfil/', views.ProfileView.as_view(), name='profile'),
    path('buscar-usuario/', views.searchUser, name="buscar-usuario"),
    path("buscar-livro/", views.searchBook, name="buscar-livro"),
]
