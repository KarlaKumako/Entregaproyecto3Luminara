from django.contrib import admin
from django.urls import path, include
from APPMagic.views import Profesor, Curso, Estudiante, Casa, home

urlpatterns = [
    path('', home, name='Home'),
    path('Curso/', Curso, name='Curso'),
    path('Estudiante/', Estudiante, name='Estudiante'),
    path('Profesor/', Profesor, name='Profesor'),
    path('Casa/', Casa, name='Casa'),
]
