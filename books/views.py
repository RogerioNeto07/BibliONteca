from django.shortcuts import render

# Create your views here.

def ViewDetailBook(request):
    return render(request, "books/detail.html")