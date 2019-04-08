import hashlib

from django.core.mail import send_mail
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from flyproject2 import settings
from jie.models import TopicInfo
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


def doreg(request):
    userinfo = UserInfo()

    userinfo.email = request.POST.get('email')
    userinfo.nickname = request.POST.get('username')

    passwd = request.POST.get('pass')
    ustr = passwd.encode(encoding='utf-8')
    m = hashlib.md5(ustr)
    passwd_md5 = m.hexdigest()

    userinfo.passwd = passwd_md5

    userinfo.save()

    # 发送验证邮件
    subject = 'fly社区欢迎您'
    message = ''
    sender = settings.DEFAULT_FROM_EMAIL
    receiver = [userinfo.email]
    html_message = '<h1>请激活：</h1><br/> ' \
                   '<a href="http://127.0.0.1:8000/user/activate/%s">' \
                   'http://127.0.0.1:8000/user/activate/%s' \
                   '<a>' % (userinfo.id, userinfo.id)

    print(html_message)

    send_mail(subject, message, sender, receiver, html_message=html_message)

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

    if not db:
        content = {
            'status': 1,
            'msg': '用户不存在！'
        }

    elif db[0].is_active == 0:
        content = {
            'status': 0,
            'action': '/user/activate/',
        }
    else:
        userinfo = {
            'id': db[0].id,
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

        # 根据用户id，取得所有的帖子，放入session

        db = TopicInfo.objects.filter(user=db[0].id)

        if db:
            topicnum = TopicInfo.objects.filter(user=db[0].id, is_delete=0).count()

            print(topicnum)

            topicinfo = []

            for d in db:
                topic = {
                    'title': d.title,
                    'content': d.content,
                    'is_delete': d.is_delete,
                    'view_times': d.view_times,
                    'kiss_num': d.kiss_num,
                    'is_top': d.is_top,
                    'is_good': d.is_good,
                    'is_over': d.is_over,
                    'comment_num': d.comment_num,
                    'create_time': d.create_time.strftime('%Y-%m-%d %H:%I:%S'),
                    # 'category': d.category,
                }

                topicinfo.append(topic)

            request.session['topicinfo'] = topicinfo
            request.session['topicnum'] = topicnum

        content = {
            'status': 0,
            'action': '/user/index/',
        }

    ret = JsonResponse(content)

    return HttpResponse(ret)


def doactivate(request, token):
    print('--->', token)

    userinfo = UserInfo.objects.get(id=token)

    userinfo.is_active = 1
    userinfo.save()

    return render(request, 'html/user/login.html')


def upload(request):
    # 从session中获取当前用户的id
    s = request.session.get('userinfo')
    uid = s['id']

    # 根据id获得对应的用户对象
    u = UserInfo.objects.get(id=uid)

    # 保存上传的文件
    u.photo = request.FILES.get('file')

    # 将上传文件保存到DB
    u.save()

    # 将改变的头像路径写入session
    s['photo'] = u.photo.url

    print(s['photo'])

    request.session['userinfo'] = s

    content = {
        'status': 0,
    }

    ret = JsonResponse(content)

    return HttpResponse(ret)
