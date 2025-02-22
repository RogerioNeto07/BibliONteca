from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from library.permissions import GroupRequiredMixin
from django.views import View
from django.http import HttpResponseBadRequest
from library.models import Emprestimo, Categoria, Livro


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
        context['categorias'] = Categoria.objects.all()

        categorias = Categoria.objects.all()
        livros_por_categoria = {}
        for categoria in categorias:
            livros = Livro.objects.filter(categoria=categoria)
            if livros.exists():
                livros_por_categoria[categoria.nome] = livros
        context['livros_por_categoria'] = livros_por_categoria
        
        return context

class PerfilView(GroupRequiredMixin, LoginRequiredMixin, TemplateView):
    template_name = "user/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.request.user
        context["usuario"] = usuario
        return context
    
class AtualizarFotoPerfilView(LoginRequiredMixin, View):
    def post(self, request):
        usuario = request.user
        if 'foto_perfil' in request.FILES:
            usuario.foto_perfil = request.FILES['foto_perfil']
            usuario.save()
            return redirect('user:profile-user')
        return HttpResponseBadRequest("Nenhuma imagem foi enviada.")

class NotificationsView(LoginRequiredMixin, TemplateView):
    template_name = "user/notifications.html"

class SearchView(TemplateView):
    template_name = 'user/search.html'

    def get(self, request, *args, **kwargs):

        categoria = request.GET.get('categoria')
        titulo = request.GET.get('titulo')
        autor = request.GET.get('autor')

        livros = Livro.objects.all()

        if categoria:
            livros = livros.filter(categoria_id=categoria)

        if titulo:
            livros = livros.filter(titulo__icontains=titulo)

        if autor:
            livros = livros.filter(autor__icontains=autor)

        return self.render_to_response({'livros': livros})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categorias"] = Categoria.objects.all()
        return context

class BookHistoryView(LoginRequiredMixin, TemplateView):
    template_name = "user/bookhistory.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['emprestimos'] = Emprestimo.objects.filter(usuario=self.request.user)
        return context

