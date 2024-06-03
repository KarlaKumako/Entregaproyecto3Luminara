from django.contrib import admin
from django.urls import path, include
from APPMagic.views import Profesores, Cursos, Estudiantes, Casa, home, Registrate, Contacto, Postulantes, Postulate,Estudiantesnuevos,Postulantes,Buscacursos

urlpatterns = [
    path('', home, name='Home'),
    path('Curso/', Cursos, name='Curso'),    
    path('Buscacursos/', Buscacursos, name='Buscacursos'),
    path('Estudiante/', Estudiantes, name='Estudiante'),
    path('Profesor/', Profesores, name='Profesor'),
    path('Casa/', Casa, name='Casa'),
    path('Registrate/', Registrate, name='Registrate'),
    path('Estudiantesnuevos/', Estudiantesnuevos, name='Estudiantesnuevos'),
    path('Contacto/', Contacto, name='Contacto'),
    path('Postulantes/', Postulantes, name='Postulantes'),
    path('Postulate/', Postulate, name='Postulate'),   
]

