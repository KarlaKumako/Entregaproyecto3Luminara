from django.contrib import admin
from django.urls import path, include
from APPMagic.views import *
from . import views


urlpatterns = [
    path('', home, name='Home'),
    
    path('Curso/', Cursos, name='Curso'),    
    path('Readmorecursos/', views.grupos_y_cursos_view, name='grupos_y_cursos_view'),
    path('crear_curso/', views.crear_curso, name='crear_curso'),
    path('mensajecursocreado/', views.mensajecursocreado, name='mensajecursocreado'),
    path('eliminar_curso/<int:id>/', views.eliminar_curso, name='eliminar_curso'),
    path('editar_curso/<int:id>/', views.editar_curso, name='editar_curso'),

    path('crear_grupo/', views.crear_grupo, name='crear_grupo'),  
    path('mensajegrupocreado/', views.mensajegrupocreado, name='mensajegrupocreado'),  
    path('eliminar_grupo/<int:id>/', views.eliminar_grupo, name='eliminar_grupo'),
    path('editar_grupo/<int:id>/', views.editar_grupo, name='editar_grupo'),



    path('Estudiante/', Estudiantes, name='Estudiante'),
    path('Registrate/', Registrate, name='Registrate'),
    path('Estudiantesnuevos/', views.estudiantes_view, name='estudiantes_view'),
    path('mensajeestudiantesnuevos/', views.mensajeestudiantesnuevos, name='mensajeestudiantesnuevos'),
    path('editar_estudiante/<int:id>/', views.editar_estudiante, name='editar_estudiante'),
    path('estudiantes_eliminar/<int:id>/', views.eliminar_estudiante, name='eliminar_estudiante'),

    path('Profesor/', Profesores, name='Profesor'),
    path('Postulados/', views.profesores_view, name='profesores_view'),
    path('Postulate/', Postulate, name='Postulate'),
    path('mensajepostulado/', mensajepostulado, name='mensajepostulado'),
    path('eliminar_profesor/<int:id>', views.eliminar_profesor, name='eliminar_profesor'),
    path('editar_profesor/<int:id>', views.editar_profesor, name='editar_profesor'),

  
    
    path('Casa/', Casa, name='Casa'),
    
    
    path('Contacto/', Contacto, name='Contacto'),
    path('mensajecontacto/', mensajecontacto, name='mensajecontacto'),
     
]

