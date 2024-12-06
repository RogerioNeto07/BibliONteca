from django.shortcuts import render

def ViewDetailBook(request):
    return render(request, "books/detail.html")

def ViewFeedbackBook(request):
    return render(request, "books/feedback.html")