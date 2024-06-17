from django.contrib import admin
from django.urls import path, include
from APPMagic.views import *
from . import views

urlpatterns = [
    path('', home, name='Home'),
    
    path('Curso/', Cursos, name='Curso'),    
    path('Buscacursos/', Buscacursos, name='Buscacursos'),

    path('Estudiante/', Estudiantes, name='Estudiante'),
    path('Registrate/', Registrate, name='Registrate'),
    path('Estudiantesnuevos/', Estudiantesnuevos, name='Estudiantesnuevos'),
    path('Profesor/', Profesores, name='Profesor'),
    path('Postulados/', profesores_view, name='Postulados'),

  
    
    path('Casa/', Casa, name='Casa'),
    
    path('Estudiantesnuevos/', Estudiantesnuevos, name='Estudiantesnuevos'),
    path('Contacto/', Contacto, name='Contacto'),
     
]

