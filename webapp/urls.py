from django.contrib import admin
from django.urls import path
from webapp.views import (Home, Auth)
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import  path
from direction.views import (AddTutor, AddAlumno)

urlpatterns = [
    path(r'inscribete/', Auth.as_view()),
    path(r'addtutor/', AddTutor.as_view()),
    path(r'addalumno/', AddAlumno.as_view()),
    path(r'', Home.as_view()),
]
