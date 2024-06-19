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
    path('Postulados/', views.profesores_view, name='profesores_view'),
    path('Postulate/', Postulate, name='Postulate'),
    path('mensajepostulado/', mensajepostulado, name='mensajepostulado'),
    path('eliminar_profesor/<int:id>', views.eliminar_profesor, name='eliminar_profesor'),
    path('editar_profesor/<int:id>', views.editar_profesor, name='editar_profesor'),

  
    
    path('Casa/', Casa, name='Casa'),
    
    path('Estudiantesnuevos/', Estudiantesnuevos, name='Estudiantesnuevos'),
    path('Contacto/', Contacto, name='Contacto'),
     
]

