from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "library/index.html")

def register(request):
    return render(request, "library/register_user.html")

def registerBook(request):
    return render(request, "library/register_book.html")

def loanBook(request):
    return render(request, 'library/loan_book.html')

def returnBook(request):
    return render(request, 'library/return_book.html')

def renewBook(request):
    return render(request, "library/renew_book.html")

def listBooks(request):
    return render(request, 'library/list_book.html')


def listUser(request):
    return render(request, 'library/list_user.html')

def pendenceUser(request):
    return render(request, 'library/pendence_user.html')