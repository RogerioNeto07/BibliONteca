from django.shortcuts import render, get_object_or_404
from .models import Livro

def ViewDetailBook(request, id):
    livro = get_object_or_404(Livro, id=id)
    context = {"livro" : livro}
    return render(request, "books/detail.html", context)

def ViewFeedbackBook(request):
    return render(request, "books/feedback.html")