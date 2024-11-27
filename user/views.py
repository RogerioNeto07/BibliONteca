from django.shortcuts import render

# Create your views here.
def IndexReader(request):
    return render(request, "user/index.html")

def IndexGuest(request):
    return render(request, "user/indexguest.html")

def Login(request):
    return render(request, "user/login.html")