from django.http import HttpResponse
from django.shortcuts import render
from .models import import Profesor, Curso, Estudiante, Casa
from PIL import Image

def home(req):
    return render(req, 'home.html')

def lista_profesores(req):
    profesores = Profesor.objects.all()
    return render(req, 'profesores.html', {'profesores': profesores})

def lista_cursos(req):
    cursos = Curso.objects.all()
    return render(req, 'cursos.html', {'cursos': cursos})

def lista_estudiantes(req):
    estudiantes = Estudiante.objects.all()
    return render(req, 'estudiantes.html', {'estudiantes': estudiantes})
