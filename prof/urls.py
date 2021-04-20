from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url('new/', views.New_excursion, name='new-excursion'),
    url(r'^edit/$', views.Profile_update, name='edit-profile'),
    url(r'^(?P<pk>\d+)/$', views.Profile_detail, name='profile-detail'),
    url(r'^(?P<pk>\d+)/excursions/$', views.Excursions, name='profile-excursions'),
    url(r'^excursions/$', views.My_excursions, name='my-profile-excursions'),
    url('', views.My_profile, name='my-profile'),
]