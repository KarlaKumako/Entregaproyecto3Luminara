from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Profesor, Curso, Estudiante, Casa
from .forms import Estudianteformulario,Contactenosformulario

def home(req):
    return render(req, 'home.html')

def Profesor(req):    
    return render(req, 'Profesor.html',{})

def Curso(req):
    return render(req, 'Curso.html', {})

def Estudiante(req):
    return render(req, 'Estudiante.html', {})

def Casa(req):
    return render(req, 'Casa.html', {})


def Registrate(request):
    if request.method == 'POST':
        form = Estudianteformulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Home')  # Cambia 'registro_exitoso' al nombre de la vista adecuada
    else:
        form = Estudianteformulario()

    return render(request, 'Registrate.html', {'form': form})

def Contacto(request):
    if request.method == 'POST':
        formulariocontacto = Contactenosformulario(request.POST)
        if formulariocontacto.is_valid():
            formulariocontacto.save()
            return redirect('Home')  # Cambia 'registro_exitoso' al nombre de la vista adecuada
    else:
        formulariocontacto = Contactenosformulario()

    return render(request, 'Contacto.html', {'formulariocontacto': formulariocontacto})