from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "library/index.html")

def register(request):
    return render(request, "library/registerUser.html")

def registerBook(request):
    return render(request, "library/registerBook.html")

def loanBook(request):
    return render(request, 'library/loanBook.html')

def returnBook(request):
    return render(request, 'library/returnBook.html')

def renewBook(request):
    return render(request, "library/renewBook.html")
