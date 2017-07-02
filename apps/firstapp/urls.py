from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^friends$', views.friends),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^users/(?P<id>\d+)$', views.viewprofile),
    url(r'^logout$', views.logout),
    url(r'^users/add/(?P<id>\d+)$', views.addfriend),
    url(r'^remove/(?P<id>\d+)$', views.removefriend),
]
