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


def dologin(request):
    email = request.POST.get('email')

    passwd = request.POST.get('pass')
    ustr = passwd.encode(encoding='utf-8')
    m = hashlib.md5(ustr)
    passwd_md5 = m.hexdigest()

    db = UserInfo.objects.filter(email=email, passwd=passwd_md5)

    if (not db):
        content = {
            'status': 1,
            'msg': '用户不存在！'
        }

    else:
        userinfo = {
            'email': db[0].email,
            'nickname': db[0].nickname,
            'city': db[0].city,
            'sign': db[0].sign,
            'gender': db[0].gender,
            'photo': db[0].photo.url,
            'qq': db[0].qq,
            'weibo': db[0].weibo,
            'join_time': db[0].join_time.strftime('%Y-%m-%d %H:%I:%S'),
            'kiss_num': db[0].kiss_num,
            'vip_grade': db[0].vip_grade,
            'is_bigv': db[0].is_bigv,
            'is_active': db[0].is_active,
        }

        request.session['userinfo'] = userinfo

        content = {
            'status': 0,
            'action': '/user/index/',
        }

    ret = JsonResponse(content)

    return HttpResponse(ret)
