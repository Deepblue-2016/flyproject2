from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'html/index.html')


def activate(request):
    return render(request, 'html/user/activate.html')


def forget(request):
    return render(request, 'html/user/forget.html')


def home(request):
    return render(request, 'html/user/home.html')


def uindex(request):
    return render(request, 'html/user/index.html')


def login(request):
    return render(request, 'html/user/login.html')


def message(request):
    return render(request, 'html/user/message.html')


def reg(request):
    return render(request, 'html/user/reg.html')


def set(request):
    return render(request, 'html/user/set.html')
