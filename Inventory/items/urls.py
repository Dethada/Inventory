from django.conf.urls import url, include
from  . import views
from django.contrib.auth.views import login
from account.views import *

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^details/(?P<id>\w{0,50})/$', views.details)
    url(r'add', views.add, name='add'),
    url(r'(?P<pk>[0-9]+)/delete', views.delete, name='delete'),
    url(r'(?P<pk>[0-9]+)/edit', views.edit, name='edit'),
    url(r'(?P<pk>[0-9]+)/increment', views.increment, name='increment'),
    url(r'(?P<pk>[0-9]+)/decrement', views.decrement, name='decrement'),
    url(r'^login/', login),
]
