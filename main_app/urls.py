from django.conf.urls import url, include
from . import views

patterns = [
    url(r'^$', views.index, name='index'),
    url(r'^history/$', views.index, name='history'),
    url(r'^team/$', views.team, name='team')
]

urlpatterns = [
    url(r'^', include(patterns, namespace='main_app', app_name='main_app')),
]
