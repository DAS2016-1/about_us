"""about_us URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import  include, url
from django.contrib import admin
from . import views

app_name = 'au_auth'
urlpatterns = [
    url(r'^login/', views.make_login, name='make_login'),
    url(r'^logout/', views.make_logout, name='make_logout'),
    url(r'^singup/', views.singup, name='singup'),
    url(r'^profiles/', views.show_profiles, name='show_profiles'),
    url(r'(?P<profile_pk>[0-9]+)/$', views.show_profile, name='show_profile'),
    url(r'^', views.index, name='index'),
]
