from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .forms import EmprestimoForm
from books.models import Livro, Categoria
from user.forms import LeitorForm
from user.models import Leitor
from .models import Emprestimo
from django.utils.timezone import now, timedelta
from django.utils import timezone
import re


def home(request):
    return render(request, "library/index.html")

def register(request):
    if request.method == "POST":
        form = LeitorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listUser")
    else:
        form = LeitorForm()
    
    return render(request, "library/users/register_user.html", {"form": form})

def registerBook(request):
    if request.method == 'POST':
        form = LivroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listBooks')
    else:
        form = LivroForm()

    categorias = Categoria.objects.all()
    return render(request, "library/books/register_book.html", {'form': form, "categorias" : categorias})


def searchUser(request):
    if request.method == "GET": 
        cpf = request.GET.get("leitor", "").strip()
        
        if not cpf:
            return JsonResponse({"erro": "CPF não fornecido"}, status=400)
        
        cpf = re.sub(r'\D', '', cpf)

        usuario = Leitor.objects.filter(cpf=cpf).first()
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


def loanBook(request):        
    if request.method == "POST":
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            emprestimo = form.save(commit=False)
            emprestimo.previsao_devolucao = now().date() + timedelta(days=15)
            emprestimo.save()
            return redirect('allLoans')
    else:
        form = EmprestimoForm()

    return render(request, 'library/books/loan_book.html', {'form': form})

def returnBook(request):
    if request.method == 'POST':
        form = DevolucaoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data.get('nome')
            isbn = form.cleaned_data.get('isbn')
            leitor = get_object_or_404(Leitor, nome=nome)
            livro = get_object_or_404(Livro, isbn=isbn)
            emprestimo = get_object_or_404(Emprestimo, livro=livro, leitor=leitor, status_ativo=True)
            emprestimo.devolver_livro()  
            emprestimo.data_devolucao = now().date()
            emprestimo.save()
            return redirect("allLoans")
    else:
        form = DevolucaoForm()
    
    return render(request, 'library/books/return_book.html', {"form" : form})

def renewBook(request):
    if request.method == 'POST':
        form = RenovarForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data.get('nome')
            isbn = form.cleaned_data.get('isbn')
            leitor = get_object_or_404(Leitor, nome=nome)
            livro = get_object_or_404(Livro, isbn=isbn)
            emprestimo = get_object_or_404(Emprestimo, livro=livro, leitor=leitor, status_ativo=True)
            if emprestimo.renovar(): 
                return redirect("allLoans")
    else:
        form = RenovarForm()
    
    return render(request, "library/books/renew_book.html", {"form" : form})

def listBooks(request):
    titulo = request.GET.get("titulo", "")
    autor = request.GET.get("autor", "")
    categoria = request.GET.get("categoria", "")
    ano = request.GET.get("ano", "")

    livros = Livro.objects.all()

    if titulo:
        livros = livros.filter(titulo__icontains=titulo)
    if autor:
        livros = livros.filter(autor__icontains=autor)
    if categoria:
        livros = livros.filter(categoria__icontains=categoria)
    if ano:
        livros = livros.filter(ano_publicacao=ano)

    return render(request, "library/books/list_book.html", {"livros": livros})

def listUser(request):
    leitores = Leitor.objects.all()
    context = {'leitores' : leitores}
    return render(request, 'library/users/list_user.html', context)

def pendenceUser(request):
    return render(request, 'library/users/pendence_user.html')

def allLoans(request):
    emprestimos = Emprestimo.objects.all()
    context = {'emprestimos' : emprestimos}
    return render(request, 'library/loans/all_loans.html', context)

def pendencesBook(request):
    emprestimos = Emprestimo.objects.filter(previsao_devolucao__lt=timezone.now(), status_ativo = True)
    context = {'emprestimos' : emprestimos}
    return render(request, 'library/loans/pendences_book.html', context)

def detailsPendencesUser(request):
    return render(request, 'library/details/details_pendences_user.html')

def detailsPendencesBook(request):
    return render(request, 'library/details/details_pendences_books.html')

def profile(request):
    return render(request, 'library/users/profile.html')
