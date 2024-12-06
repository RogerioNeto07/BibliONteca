from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "library/books/index.html")

def register(request):
    return render(request, "library/users/register_user.html")

def registerBook(request):
    return render(request, "library/books/register_book.html")

def loanBook(request):
    return render(request, 'library/books/loan_book.html')

def returnBook(request):
    return render(request, 'library/books/return_book.html')

def renewBook(request):
    return render(request, "library/books/renew_book.html")

def listBooks(request):
    return render(request, 'library/books/list_book.html')

def listUser(request):
    return render(request, 'library/users/list_user.html')

def pendenceUser(request):
    return render(request, 'library/users/pendence_user.html')

def allLoans(request):
    return render(request, 'library/loans/all_loans.html')

def pendences_book(request):
    return render(request, 'library/loans/pendences_book.html')