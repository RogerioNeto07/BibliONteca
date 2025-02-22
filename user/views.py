from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from library.permissions import GroupRequiredMixin
from library.models import Livro, Categoria


class LoginView(TemplateView):
    template_name = "user/login.html"
        
    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(data=request.POST)
        
        if form.is_valid():
            email = form.cleaned_data['username']  
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            login(request, user)
            return redirect('user:home')
        else:
            return HttpResponse('Usuário ou senha inválidos.', status=401)
        
class HomeView(TemplateView):
    model = Livro
    template_name = "user/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['livros'] = Livro.objects.all()
        context['livros_chegados'] = Livro.objects.all().order_by('-data_cadastro')[:10]

        categorias = Categoria.objects.all()
        livros_por_categoria = {}
        for categoria in categorias:
            livros = Livro.objects.filter(categoria=categoria)
            if livros.exists():
                livros_por_categoria[categoria.nome] = livros
        context['livros_por_categoria'] = livros_por_categoria
        
        return context

class PerfilView(GroupRequiredMixin, LoginRequiredMixin, TemplateView):
    group_required = 'Bibliotecario'

    template_name = "user/profile.html"

class NotificationsView(LoginRequiredMixin, TemplateView):
    template_name = "user/notifications.html"

class SearchView(LoginRequiredMixin, TemplateView):
    template_name = "user/search.html"

class BookHistoryView(LoginRequiredMixin, TemplateView):
    template_name = "user/bookhistory.html"
