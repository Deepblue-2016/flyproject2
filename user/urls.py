from django.conf.urls import url

from user import views

urlpatterns = [
    url(r'^activate/$', views.activate),
    url(r'^forget/$', views.forget),
    url(r'^home/$', views.home),
    url(r'^index/$', views.uindex),
    url(r'^login/$', views.login),
    url(r'^message/$', views.message),
    url(r'^reg/$', views.reg),
    url(r'^set/$', views.set),

    url(r'^doreg/$', views.doreg),
    url(r'^dologin/$', views.dologin),

    url(r'^activate/(?P<token>.*)$', views.doactivate),
    url(r'^upload/$', views.upload),

    url(r'^test1/$', views.dotest1),
    url(r'^test2/$', views.dotest2),
    url(r'^test3/$', views.dotest3),

]
