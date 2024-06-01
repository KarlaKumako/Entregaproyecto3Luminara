from django.contrib import admin
from django.urls import path, include
from APPMagic.views import Profesor, Curso, Estudiante, Casa, home, Registrate, Contacto

urlpatterns = [
    path('', home, name='Home'),
    path('Curso/', Curso, name='Curso'),
    path('Estudiante/', Estudiante, name='Estudiante'),
    path('Profesor/', Profesor, name='Profesor'),
    path('Casa/', Casa, name='Casa'),
    path('Registrate/', Registrate, name='Registrate'),
    path('Contacto/', Contacto, name='Contacto'),
]

