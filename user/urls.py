from django.urls import path
from user import views

urlpatterns = [
    path('', views.Login), 
    path('pagina-inicial/', views.home, name='home'),
    path('login', views.login, name='login'),
    path('perfil', views.Perfil, name='profile-user'),
    path('notificacoes', views.Notifications, name='notifications'),
    path('pesquisa/', views.Search, name='pesquisa'),
    path('history', views.Bookhistory, name='history'),
]
