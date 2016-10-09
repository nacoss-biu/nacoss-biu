"""nacoss_biu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^', include('spirit.urls')),
	url(r'^home/', include('main_app.urls')),
	url(r'^news/', include('news.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('polls.urls')),
    url(r'^events/', include('events.urls')),
    url(r'^notice/', include('notice.urls')),
	# url(r'^blog/', include('blog.urls')),
    url(r'^blog/', include('zinnia.urls', namespace="zinnia")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
