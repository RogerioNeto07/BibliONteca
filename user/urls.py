from django.urls import path
from user import views

urlpatterns = [
    path('', views.Login, name='login'),  # Tela de login
    path('home/', views.home, name='home'),  # Página principal
    path('profile/', views.Perfil, name='profile'),  # Perfil do usuário
    path('notifications/', views.Notifications, name='notifications'),  # Notificações
    path('pesquisa/', views.Search, name='search'),  # Pesquisa
]
