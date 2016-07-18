from django.conf.urls import url, include
from . import views

patterns = [
	url(r'^$', views.index_all, name='index_all'),
]

urlpatterns = [
	url(r'^', include(patterns, namespace='notice', app_name='notice')),
]