from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^write/$', views.write, name='write'),
    url(r'^list/$', views.list, name='list'),
    url(r'^detail/(?P<pk>\d+)/$', views.detail, name='detail'),
]
