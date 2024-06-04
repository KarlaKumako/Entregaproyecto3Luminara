from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Profesor, Curso, Estudiante, Casa, Grupos
from .forms import Estudianteformulario,Contactenosformulario,ProfesorForm,BusquedaProfesorForm,EstudianteSearchForm,CursoSearchForm

#VIsta de la Home
def home(req):
    return render(req, 'home.html')

#Vistas del desplegable profesores

def Profesores(req):    
    return render(req, 'Profesor.html',{})

def Postulantes(req):    
    return render(req, 'Postulantes.html',{})

def Postulate(request):    
    if request.method == 'POST':
        formularioprofesor = ProfesorForm(request.POST)
        if formularioprofesor.is_valid():
            formularioprofesor.save()
            return redirect('Postulantes')  # Redirige a una página de éxito
    else:
        formularioprofesor = ProfesorForm()
    return render(request, 'Postulate.html', {'formularioprofesor': formularioprofesor})

def Postulantes(request):
    form = BusquedaProfesorForm(request.GET or None)
    if form.is_valid():
        # Obtiene los datos limpios del formulario
        nombre = form.cleaned_data.get('nombre')
        apellido = form.cleaned_data.get('apellido')
        profesion = form.cleaned_data.get('profesion')

        # Inicializa el queryset
        queryset = Profesor.objects.all()

        # Aplica filtros si se proporciona el campo correspondiente
        if nombre:
            queryset = queryset.filter(nombre__icontains=nombre)
        if apellido:
            queryset = queryset.filter(apellido__icontains=apellido)
        if profesion:
            queryset = queryset.filter(profesion__icontains=profesion)

        return render(request, 'resultados_postulantes.html', {'profesores': queryset})


    return render(request, 'Postulantes.html', {'form': form})

#Vistas cursos

def Cursos(req):
    return render(req, 'Curso.html', {})



def Buscacursos(request):
    if request.method == 'POST':
        form = CursoSearchForm(request.POST)
        if form.is_valid():
            curso_buscado = form.cleaned_data['curso']
            cursos = Curso.objects.filter(Curso__icontains=curso_buscado)
            return render(request, 'resultadocurso.html', {'cursos': cursos, 'curso_buscado': curso_buscado})
    else:
        form = CursoSearchForm()
    
    return render(request, 'Buscacurso.html', {'form': form})


def Estudiantes(req):
    return render(req, 'Estudiante.html', {})


def Registrate(request):
    if request.method == 'POST':
        form = Estudianteformulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Estudiantesnuevos')  # Cambia 'registro_exitoso' al nombre de la vista adecuada
    else:
        form = Estudianteformulario()

    return render(request, 'Registrate.html', {'form': form})

def Estudiantesnuevos(request):
   form = EstudianteSearchForm(request.GET or None)
   estudiantes = None
   if form.is_valid():
        nombre = form.cleaned_data.get('nombre')
        apellido = form.cleaned_data.get('apellido')
        casa = form.cleaned_data.get('casa')

        estudiantes = Estudiante.objects.all()
        if nombre:
            estudiantes = estudiantes.filter(nombre__icontains=nombre)
        if apellido:
            estudiantes = estudiantes.filter(apellido__icontains=apellido)
        if casa:
            estudiantes = estudiantes.filter(casa__nombre__icontains=casa)  # Asumiendo que 'casa' es un ForeignKey relacionado con 'Casa'
        return render(request, 'resultados_estudiantes.html', {'estudiantes': estudiantes})
   
   return render(request, 'Estudiantesnuevos.html', {'form': form, 'estudiantes': estudiantes})

#View de las casas
def Casa(req):
    return render(req, 'Casa.html', {})

#View del sector contactenos

def Contacto(request):
    if request.method == 'POST':
        formulariocontacto = Contactenosformulario(request.POST)
        if formulariocontacto.is_valid():
            formulariocontacto.save()
            return redirect('Home')  # Cambia 'registro_exitoso' al nombre de la vista adecuada
    else:
        formulariocontacto = Contactenosformulario()

    return render(request, 'Contacto.html', {'formulariocontacto': formulariocontacto})