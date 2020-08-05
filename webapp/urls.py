from django.contrib import admin
from django.urls import path
from webapp.views import (Home, Inscribete)
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import  path
from direction.views import (AddTutor, AddAlumno)
from .views import (AuthParent, ParentHome)


urlpatterns = [
    path(r'inscribete/', Inscribete.as_view()),
    path(r'addtutor/', AddTutor.as_view()),
    path(r'addalumno/', AddAlumno.as_view()),
    path(r'auth/', AuthParent.as_view()),
    path(r'parent/', ParentHome.as_view(), name='parent'),
    path(r'', Home.as_view()),
]
