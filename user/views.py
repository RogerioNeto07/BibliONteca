from django.shortcuts import render

# Create your views here.
def IndexReader(request):
    return render(request, "user/index.html")

def IndexGuest(request):
    return render(request, "user/indexguest.html")

def Login(request):
    return render(request, "user/login.html")
def home(request):
    return render(request, "user/home.html")

def index(request):
    return render(request, "user/index.html")

def login(request):
    return render(request, "user/login.html")

def Perfil(request):
    return render(request, "user/profile.html")

def Notifications(request):
    return render(request, "user/notifications.html")
