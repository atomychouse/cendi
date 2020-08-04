from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from direction.views import (Home, Login, Inscripcion)
from django.urls import  (path, re_path)


urlpatterns = [
    path(r'login/', Login.as_view()),
    path(r'inscripciones/', Inscripcion.as_view()),
    path(r'', Home.as_view()),
]
