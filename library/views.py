from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.models import Group
from django.utils.timezone import now, timedelta
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView
from django.views.generic.edit import FormView

from .forms import EmprestimoForm, LivroForm, DevolucaoForm, RenovarForm
from .models import Livro, Categoria
from .models import Emprestimo
from user.forms import UserRegisterForm
from .permissions import GroupRequiredMixin


User = get_user_model()

class HomeView(TemplateView):
    template_name = "library/index.html"


class ViewFeedbackBook(TemplateView):
    login_url = reverse_lazy('user:login')
    template_name = "library/books/feedback.html"

class ViewDetailBook(TemplateView):
    login_url = reverse_lazy('user:login')
    template_name = "library/books/detail.html"

class RegisterView(GroupRequiredMixin, LoginRequiredMixin, FormView):
    group_required = 'Bibliotecario'
    template_name = "library/users/register_user.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("library:listUser")

    def form_valid(self, form):
        user = form.save()
        grupo, _ = Group.objects.get_or_create(name="Usuarios")
        user.groups.add(grupo)
        messages.success(self.request, "Cadastro realizado com sucesso! Faça login para continuar.")
        login(self.request, user)
        return super().form_valid(form)
    
class ListUserView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = User
    group_required = 'Bibliotecario'
    template_name = "library/users/list_user.html"
    context_object_name = "usuarios"

class RegisterBookView(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Livro
    group_required = 'Bibliotecario'
    form_class = LivroForm
    template_name = "library/books/register_book.html"
    success_url = reverse_lazy("library:listBooks")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categorias"] = Categoria.objects.all()
        return context

class LoanBookView(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    form_class = EmprestimoForm
    group_required = 'Bibliotecario'
    template_name = "library/books/loan_book.html"
    success_url = reverse_lazy("library:allLoans")

    def form_valid(self, form):
        emprestimo = form.save(commit=False)
        emprestimo.usuario = self.request.user
        emprestimo.save()
        return super().form_valid(form)

class ReturnBookView(GroupRequiredMixin, LoginRequiredMixin, FormView):
    template_name = "library/books/return_book.html"
    group_required = 'Bibliotecario'
    form_class = DevolucaoForm
    success_url = reverse_lazy("library:allLoans")

    def form_valid(self, form):
        nome = form.cleaned_data["nome"]
        isbn = form.cleaned_data["isbn"]

        usuario = get_object_or_404(User, nome=nome)
        livro = get_object_or_404(Livro, isbn=isbn)

        emprestimo = get_object_or_404(Emprestimo, livro=livro, usuario=usuario, status_ativo=True)
        emprestimo.status_ativo = False
        emprestimo.data_devolucao = now().date()
        emprestimo.save()

        return super().form_valid(form)

class RenewBookView(GroupRequiredMixin, LoginRequiredMixin, FormView):
    template_name = "library/books/renew_book.html"
    group_required = 'Bibliotecario'
    form_class = RenovarForm
    success_url = reverse_lazy("library:allLoans")

    def form_valid(self, form):
        nome = form.cleaned_data["nome"]
        isbn = form.cleaned_data["isbn"]

        usuario = get_object_or_404(User, nome=nome)
        livro = get_object_or_404(Livro, isbn=isbn)

        emprestimo = get_object_or_404(Emprestimo, livro=livro, usuario=usuario, status_ativo=True)
        emprestimo.previsao_devolucao += timedelta(days=15)
        emprestimo.save()

        return super().form_valid(form)

class ListBooksView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Livro
    group_required = 'Bibliotecario'
    template_name = "library/books/list_book.html"
    context_object_name = "livros"

    def get_queryset(self):
        queryset = Livro.objects.all()
        titulo = self.request.GET.get("titulo", "")
        autor = self.request.GET.get("autor", "")
        categoria = self.request.GET.get("categoria", "")
        ano = self.request.GET.get("ano", "")

        if titulo:
            queryset = queryset.filter(titulo__icontains=titulo)
        if autor:
            queryset = queryset.filter(autor__icontains=autor)
        if categoria:
            queryset = queryset.filter(categoria__nome__icontains=categoria)
        if ano:
            queryset = queryset.filter(ano_publicacao=ano)

        return queryset

class PendenceUserView(GroupRequiredMixin, LoginRequiredMixin, TemplateView):
    group_required = 'Bibliotecario'
    template_name = "library/users/pendence_user.html"

class AllLoansView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Emprestimo
    group_required = 'Bibliotecario'
    template_name = "library/loans/all_loans.html"
    context_object_name = "emprestimos"

class PendencesBookView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = 'Bibliotecario'
    template_name = "library/loans/pendences_book.html"
    context_object_name = "emprestimos"

    def get_queryset(self):
        return Emprestimo.objects.filter(previsao_devolucao__lt=timezone.now(), status_ativo=True)

class DetailsPendencesUserView(GroupRequiredMixin, LoginRequiredMixin, TemplateView):
    group_required = 'Bibliotecario'
    template_name = "library/details/details_pendences_user.html"

class DetailsPendencesBookView(GroupRequiredMixin, LoginRequiredMixin, TemplateView):
    group_required = 'Bibliotecario'
    template_name = "library/details/details_pendences_books.html"

class ProfileView(GroupRequiredMixin, LoginRequiredMixin, TemplateView):
    template_name = "library/users/profile.html"
