"""search URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from search import views
from search.models import Excursion

urlpatterns = [
    url(r'^excursion/(?P<pk>\d+)/edit/$', views.Excursion_update, name='excursion-edit'),
    url(r'^excursion/(?P<pk>\d+)/check/$', views.Excursion_check, name='excursion-check'),
    url(r'^excursion/(?P<pk>\d+)$', views.Excursion_detail, name='excursion-detail'),
    url('', views.Excursions, name='excursion'),
]
