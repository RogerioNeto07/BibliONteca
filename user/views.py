from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from library.permissions import GroupRequiredMixin
from django.views import View
from django.http import HttpResponseBadRequest
from library.models import Emprestimo


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
    template_name = "user/home.html"

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

class SearchView(LoginRequiredMixin, TemplateView):
    template_name = "user/search.html"

class BookHistoryView(LoginRequiredMixin, TemplateView):
    template_name = "user/bookhistory.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['emprestimos'] = Emprestimo.objects.filter(usuario=self.request.user)
        return context

