from django.shortcuts import render

# Create your views here.

def TesteBase(request):
    return render(request, "user/index.html")