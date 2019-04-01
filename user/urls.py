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

    url(r'^doset/$', views.doset),

]
