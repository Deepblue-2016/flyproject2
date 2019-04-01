import hashlib

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from user.models import UserInfo


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


def doset(request):
    userinfo = UserInfo()

    userinfo.email = request.POST.get('email')
    userinfo.nickname = request.POST.get('username')

    passwd = request.POST.get('pass')
    ustr = passwd.encode(encoding='utf-8')
    m = hashlib.md5(ustr)
    passwd_md5 = m.hexdigest()

    userinfo.passwd = passwd_md5

    userinfo.save()

    content = {
        'status': 0,
        'action': '/user/login/',
    }

    ret = JsonResponse(content)

    return HttpResponse(ret)
