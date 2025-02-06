from django.shortcuts import render, redirect
from .forms import LivroForm
from .forms import EmprestimoForm
from books.models import Livro, Categoria
from user.forms import LeitorForm
from user.models import Leitor
from .models import Emprestimo

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

def loanBook(request):
    if request.method == "POST":
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            emprestimo = form.save(commit=False)
            emprestimo.save()
            return redirect('allLoans')
    else:
        form = EmprestimoForm()

    return render(request, 'library/books/loan_book.html', {'form': form})

def returnBook(request):
    return render(request, 'library/books/return_book.html')

def renewBook(request):
    return render(request, "library/books/renew_book.html")

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
    return render(request, 'library/loans/pendences_book.html')

def detailsPendencesUser(request):
    return render(request, 'library/details/details_pendences_user.html')

def detailsPendencesBook(request):
    return render(request, 'library/details/details_pendences_books.html')

def profile(request):
    return render(request, 'library/users/profile.html')