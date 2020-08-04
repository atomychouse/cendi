from django.contrib import admin
from django.urls import path
from webapp.views import (Home, Parent, Auth)
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import  path


urlpatterns = [
    path(r'auth_parent/', Auth.as_view()),
    path(r'home_parent/', Parent.as_view()),
    path(r'', Home.as_view()),
]
