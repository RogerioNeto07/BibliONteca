from django.shortcuts import render, redirect
from .forms import LivroForm
from books.models import Livro

def home(request):
    return render(request, "library/index.html")

def register(request):
    return render(request, "library/users/register_user.html")

def registerBook(request):
    if request.method == 'POST':
        form = LivroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listBooks')
    else:
        form = LivroForm()
    return render(request, "library/books/register_book.html", {'form': form})

def loanBook(request):
    return render(request, 'library/books/loan_book.html')

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
    return render(request, 'library/users/list_user.html')

def pendenceUser(request):
    return render(request, 'library/users/pendence_user.html')

def allLoans(request):
    return render(request, 'library/loans/all_loans.html')

def pendencesBook(request):
    return render(request, 'library/loans/pendences_book.html')

def detailsPendencesUser(request):
    return render(request, 'library/details/details_pendences_user.html')

def detailsPendencesBook(request):
    return render(request, 'library/details/details_pendences_books.html')

def profile(request):
    return render(request, 'library/users/profile.html')