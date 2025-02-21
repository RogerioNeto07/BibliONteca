from django.urls import path
from django.contrib.auth.views import LogoutView

from user import views

app_name = 'user'

urlpatterns = [
    path('login', views.LoginView.as_view(), name='login'), 
    path('', views.HomeView.as_view(), name='home'),
    path('perfil', views.PerfilView.as_view(), name='profile-user'),
    path('notificacoes', views.NotificationsView.as_view(), name='notifications'),
    path('pesquisa/', views.SearchView.as_view(), name='pesquisa'),
    path('history', views.BookHistoryView.as_view(), name='history'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
