from django.http import HttpResponse
from django.shortcuts import render
from .models import Profesor, Curso, Estudiante, Casa
from PIL import Image

def home(req):
    return render(req, 'home.html')

def lista_profesores(req):
    #profesores = Profesor.objects.all()
    return render(req, 'Profesor.html', {'profesores': profesores})

def lista_cursos(req):
    #cursos = Curso.objects.all()
    return render(req, 'Curso.html', {'cursos': cursos})

def lista_estudiantes(req):
    #estudiantes = Estudiante.objects.all()
    return render(req, 'Estudiante.html', {'estudiantes': estudiantes})

def Casa(req):
    return render(req, 'Casa.html', {})