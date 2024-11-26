from django.shortcuts import render

# Create your views here.

def IndexReader(request):
    return render(request, "user/indexreader.html")

def IndexLibrarian(request):
    return render(request, "user/indexlibrarian.html")

def IndexLoggedOut(request):
    return render(request, "user/indexloggedout.html")