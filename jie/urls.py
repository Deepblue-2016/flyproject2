from django.conf.urls import url

from jie import views

urlpatterns = [
    url(r'^index/$', views.jindex),
    url(r'^add/$', views.add),
    url(r'^detail/$', views.detail),
]
