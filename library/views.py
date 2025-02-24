from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import Group
from django.utils.timezone import now, timedelta
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from django.db.models import Count, Q
from django.db.models import F, ExpressionWrapper, fields
from django.db.models.functions import Now
import re
from .forms import EmprestimoForm, LivroForm, DevolucaoForm, RenovarForm, UsuarioUpdateForm
from .models import Livro, Categoria, Comentarios
from .models import Emprestimo
from user.forms import UserRegisterForm
from user.models import MyUser
from .permissions import GroupRequiredMixin
from django.shortcuts import render, get_object_or_404
from user.utils import adicionar_notificacao


User = get_user_model()

class HomeView(TemplateView):
    template_name = "library/index.html"

class RegisterView(GroupRequiredMixin, LoginRequiredMixin, FormView):
    group_required = 'Bibliotecario'
    template_name = "library/users/register_user.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("library:listUser")

    def form_valid(self, form):
        user = form.save()
        grupo, _ = Group.objects.get_or_create(name="Usuarios")
        user.groups.add(grupo)
        messages.success(self.request, "Cadastro realizado com sucesso!")
        return super().form_valid(form)
    
class ListUserView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = MyUser
    group_required = 'Bibliotecario'
    template_name = "library/users/list_user.html"
    context_object_name = "usuarios"

    def get_queryset(self):
        nome = self.request.GET.get('nome', '')
        cpf = self.request.GET.get('cpf', '')
        queryset = super().get_queryset()

        if nome:
            queryset = queryset.filter(nome__icontains=nome)
        if cpf:
            queryset = queryset.filter(cpf__icontains=cpf)
        
        return queryset
    
class UsuarioUpdateView(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = MyUser
    form_class = UsuarioUpdateForm
    group_required = 'Bibliotecario'
    template_name = 'library/users/edituser.html'
    context_object_name = 'usuario'

    def get_success_url(self):
        return reverse_lazy('library:listUser')

    
class RegisterBookView(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Livro
    group_required = 'Bibliotecario'
    form_class = LivroForm
    template_name = "library/books/register_book.html"
    success_url = reverse_lazy("library:listBooks")

    def form_valid(self, form):
        livro = form.save()
        messages.success(self.request, "Cadastro realizado com sucesso!")

        for usuario in MyUser.objects.all():
            adicionar_notificacao(
                usuario,
                f"Novo livro '{livro.titulo}' chegou!",
                "novidade"
        )

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categorias"] = Categoria.objects.all()
        return context

from user.utils import adicionar_notificacao 
class LoanBookView(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    form_class = EmprestimoForm
    group_required = 'Bibliotecario'
    template_name = "library/books/loan_book.html"
    success_url = reverse_lazy("library:allLoans")

    def form_valid(self, form):
        response = super().form_valid(form)
        
        livro = form.cleaned_data['livro']
        usuario = form.cleaned_data['usuario']
        bibliotecario = self.request.user

        adicionar_notificacao(
            bibliotecario,
            f"Você realizou o empréstimo do livro '{livro.titulo}' para {usuario.nome}.",
            "geral"
        )

        adicionar_notificacao(
            usuario,
            f"Você pegou emprestado o livro '{livro.titulo}'.",
            "geral"
        )

        messages.success(self.request, "Empréstimo realizado com sucesso!")
        return response

class ReturnBookView(GroupRequiredMixin, LoginRequiredMixin, FormView):
    template_name = "library/books/return_book.html"
    group_required = 'Bibliotecario'
    form_class = DevolucaoForm
    success_url = reverse_lazy("library:allLoans")

    def form_valid(self, form):
        usuario = form.cleaned_data["usuario"]
        livro = form.cleaned_data["livro"]
        bibliotecario = self.request.user

        emprestimo = get_object_or_404(Emprestimo, livro=livro, usuario=usuario, status_ativo=True)
        emprestimo.status_ativo = False
        emprestimo.data_devolucao = now().date()
        emprestimo.save()

        adicionar_notificacao(
            bibliotecario,
            f"Você registrou a devolução do livro '{livro.titulo}' de {usuario.nome}.",
            "geral"
        )

        adicionar_notificacao(
            usuario,
            f"Você devolveu o livro '{livro.titulo}'. Obrigado!",
            "geral"
        )

        messages.success(self.request, "Devolução registrada com sucesso!")
        return super().form_valid(form)


class RenewBookView(GroupRequiredMixin, LoginRequiredMixin, FormView):
    template_name = "library/books/renew_book.html"
    group_required = 'Bibliotecario'
    form_class = RenovarForm
    success_url = reverse_lazy("library:allLoans")

    def form_valid(self, form):
        usuario = form.cleaned_data["usuario"]
        livro = form.cleaned_data["livro"]
        bibliotecario = self.request.user

        emprestimos = Emprestimo.objects.filter(livro=livro, usuario=usuario, status_ativo=True)

        if emprestimos.count() == 1:
            emprestimo = emprestimos.first()
        else:
            return self.form_invalid(form)

        emprestimo.previsao_devolucao += timedelta(days=15)
        emprestimo.save()

        adicionar_notificacao(
            bibliotecario,
            f"Você renovou o empréstimo do livro '{livro.titulo}' de {usuario.nome}.",
            "geral"
        )

        adicionar_notificacao(
            usuario,
            f"O empréstimo do livro '{livro.titulo}' foi renovado.",
            "geral"
        )

        messages.success(self.request, "Renovação realizada com sucesso!")
        return super().form_valid(form)

class LivroUpdateView(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Livro
    form_class = LivroForm
    group_required = 'Bibliotecario'
    template_name = 'library/books/editbook.html'
    context_object_name = 'livro'
    
    def get_success_url(self):
        return reverse_lazy('library:detail-books', kwargs={'pk': self.object.pk})

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

    def get_queryset(self):
        titulo = self.request.GET.get('titulo', '')
        usuario = self.request.GET.get('usuario', '')
        status = self.request.GET.get('status', '')

        queryset = Emprestimo.objects.all()

        if titulo:
            queryset = queryset.filter(livro__titulo__icontains=titulo)
        if usuario:
            queryset = queryset.filter(usuario__nome__icontains=usuario)

        if status == 'atrasado':
            queryset = queryset.filter(
                data_devolucao__lt=timezone.now().date(), 
                status_ativo=True
            )
        elif status == 'dentro_prazo':
            queryset = queryset.filter(
                previsao_devolucao__gte=timezone.now().date(), 
                data_devolucao__isnull=True,
                status_ativo=True
            )

        return queryset


class PendencesBookView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = 'Bibliotecario'
    template_name = "library/loans/all_loans.html"
    context_object_name = "emprestimos"

    def get_queryset(self):
        queryset = Emprestimo.objects.filter(status_ativo=True)

        queryset = queryset.filter(previsao_devolucao__lt=timezone.now())

        queryset = queryset.annotate(
            dias_atraso=ExpressionWrapper(
                F('previsao_devolucao') - Now(),
                output_field=fields.DurationField()
            )
        )

        nome_livro = self.request.GET.get('nome_livro', '')
        nome_usuario = self.request.GET.get('nome_usuario', '')
        
        if nome_livro:
            queryset = queryset.filter(livro__titulo__icontains=nome_livro)
        
        if nome_usuario:
            queryset = queryset.filter(usuario__nome__icontains=nome_usuario)

        return queryset

class DetailsPendencesUserView(GroupRequiredMixin, LoginRequiredMixin, TemplateView):
    group_required = 'Bibliotecario'
    template_name = "library/details/details_pendences_user.html"

class DetailsPendencesBookView(GroupRequiredMixin, LoginRequiredMixin, TemplateView):
    group_required = 'Bibliotecario'
    template_name = "library/details/details_pendences_books.html"

class ProfileView(GroupRequiredMixin, LoginRequiredMixin, TemplateView):
    group_required = 'Bibliotecario'
    template_name = "user/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["usuario"] = self.request.user
        return context

class PerfilUsuarioView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = MyUser
    template_name = 'library/users/user.html'
    context_object_name = 'usuario'
    
    def test_func(self):
        return self.request.user.groups.filter(name='Bibliotecario').exists()

    def get_object(self, queryset=None):
        usuario_id = self.kwargs.get('usuario_id')
        return get_object_or_404(MyUser, id=usuario_id)


def ViewDetailBook(request, pk):
    livro = get_object_or_404(Livro, id=pk)
    comentarios = Comentarios.objects.filter(livro=livro)

    for comentario in comentarios:
        comentario.estrelas_preenchidas = ['★'] * comentario.estrela
        comentario.estrelas_vazias = ['☆'] * (5 - comentario.estrela)
        
    context = {
        "livro": livro,
        "comentarios": comentarios
    }
    return render(request, "library/books/detail.html", context)

def ViewFeedbackBook(request, pk):
    livro = get_object_or_404(Livro, id=pk)
    context = {"livro" : livro}
    return render(request, "library/books/feedback.html", context)

@login_required
def ViewComentarios(request, pk):
    livro = get_object_or_404(Livro, id=pk)
    user = request.user

    if request.method == "POST":
        comentario_text = request.POST.get('user-comment', '')
        star_rating = request.POST.get('star-rating')

        try:
            star_rating = int(star_rating)
        except (TypeError, ValueError):
            star_rating = 0

        if star_rating < 1 or star_rating > 5:
            star_rating = 0

        if star_rating:
            Comentarios.objects.create(
                comentario=comentario_text,
                livro=livro,
                usuario=user,
                estrela=star_rating
            )
            messages.success(request, "Seu comentário foi enviado com sucesso!")
            return redirect('library:detail-books', pk=livro.id)
        else:
            messages.error(request, "Por favor, selecione uma avaliação válida de 1 a 5 estrelas.")

    return render(request, 'library/books/feedback.html', {'livro': livro, 'user': user})

def searchUser(request):
    if request.method == "GET": 
        cpf = request.GET.get("usuario", "").strip()
        
        if not cpf:
            return JsonResponse({"erro": "CPF não fornecido"}, status=400)
        
        cpf = re.sub(r'\D', '', cpf)

        usuario = MyUser.objects.filter(cpf=cpf).first()
        if usuario:
            return JsonResponse({"nome": usuario.nome})
        else:
            return JsonResponse({"erro": "Usuário não encontrado"}, status=404)

    return JsonResponse({"erro": "Método não permitido"}, status=405)

def searchBook(request):
    if request.method == "GET":
        isbn = request.GET.get("isbn", "").strip()

        if not isbn:
            return JsonResponse({"erro": "ISBN não fornecido"}, status=400)

        livro = Livro.objects.filter(isbn=isbn).first()

        if livro:
            return JsonResponse({
                "titulo": livro.titulo,
                "imagem": livro.capa.url if livro.capa else None 
            })
        else:
            return JsonResponse({"erro": "Livro não encontrado"}, status=404)

    return JsonResponse({"erro": "Método não permitido"}, status=405)
