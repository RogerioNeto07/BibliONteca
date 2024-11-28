from django.shortcuts import render

# Create your views here.
<<<<<<< Updated upstream
def IndexReader(request):
    return render(request, "user/index.html")

def IndexGuest(request):
    return render(request, "user/indexguest.html")

def Login(request):
=======
def home(request):
    return render(request, "user/home.html")

def index(request):
    return render(request, "user/index.html")

def login(request):
>>>>>>> Stashed changes
    return render(request, "user/login.html")