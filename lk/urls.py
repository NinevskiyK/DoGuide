from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views
from search.models import Excursion
from django.urls import include

urlpatterns = [
    url('', include('django.contrib.auth.urls')),
    path('register/', views.create_profile, name="register"),
]