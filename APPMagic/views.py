from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from Proyecto3Luminara.settings import EMAIL_HOST_USER
from .models import Profesor, Curso, Estudiante, Casa, Grupos
from .forms import Estudianteformulario,Contactenosformulario,ProfesorForm,BusquedaProfesorForm,EstudianteSearchForm,CursoSearchForm
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import send_mail



#VIsta de la Home
def home(req):
    return render(req, 'home.html')

# Vistas del desplegable profesores:

# #----Vistas profesores:

def Profesores(req):    
    return render(req, 'Profesor.html',{})

# #----Vistas profesores postulantes:

def Postulantes(req):    
     return render(req, 'Postulantes.html',{})

def mensajepostulado(req):    
     return render(req, 'mensajepostulado.html',{})

# #----Vista formulario postulantes:

def Postulate(request):    
    if request.method == 'POST':
        formularioprofesor = ProfesorForm(request.POST)
        if formularioprofesor.is_valid():
            formularioprofesor.save()
            return redirect('mensajepostulado')  # Redirige a una página de éxito
    else:
        formularioprofesor = ProfesorForm()
    return render(request, 'Postulateformulario.html', {'formularioprofesor': formularioprofesor})

# #----Vista busqueda de profesores postulantes:

# def Postulantes(request):

#     form = BusquedaProfesorForm(request.GET or None)
#     if form.is_valid():
#         # Obtiene los datos limpios del formulario
#         nombre = form.cleaned_data.get('nombre')
#         apellido = form.cleaned_data.get('apellido')
#         profesion = form.cleaned_data.get('profesion')

#         queryset = Profesor.objects.all()

#         if nombre:
#             queryset = queryset.filter(nombre__icontains=nombre)
#         if apellido:
#             queryset = queryset.filter(apellido__icontains=apellido)
#         if profesion:
#             queryset = queryset.filter(profesion__icontains=profesion)

#         return render(request, 'resultadobusquedapostulado.html', {'profesores': queryset})


#     return render(request, 'listapostulados.html', {'form': form})

# #----Vista lista de profesores postulantes:

# def lista_profesores(request):

#     mis_profesores = Profesor.objects.all()

#     return render(request, 'listapostulados.html', {'profesores': mis_profesores})

def profesores_view(request):
    # Listar todos los profesores
    mis_profesores = Profesor.objects.all()

    # Manejar el formulario de búsqueda
    form = BusquedaProfesorForm(request.GET or None)
    search_results = None
    if form.is_valid():
        nombre = form.cleaned_data.get('nombre')
        apellido = form.cleaned_data.get('apellido')
        profesion = form.cleaned_data.get('profesion')        

        queryset = Profesor.objects.all()

        if nombre:
            queryset = queryset.filter(nombre__icontains=nombre)
        if apellido:
            queryset = queryset.filter(apellido__icontains=apellido)
        if profesion:
            queryset = queryset.filter(profesion__icontains=profesion)
        

        search_results = queryset

    return render(request, 'Postulados.html', {
        'mis_profesores': mis_profesores,
        'form': form,
        'search_results': search_results,
    })

#----Vista eliminar profesor:

def eliminar_profesor(request, id):
    profesor = get_object_or_404(Profesor, id=id)

    if request.method == 'POST':
        # Confirmación de la eliminación
        profesor.delete()
        messages.success(request, f'El profesor {profesor.nombre} {profesor.apellido} ha sido eliminado correctamente.')
        return redirect('profesores_view')  # Redirige a la vista de lista de profesores

    # Si el método no es POST, renderiza el template de confirmación de eliminación
    return render(request, 'eliminar_profesor.html', {'profesor': profesor})

#----Vista modificación profesor:

def editar_profesor(request, id):
    profesor = get_object_or_404(Profesor, id=id)

    if request.method == 'POST':
        formularioprofesor = ProfesorForm(request.POST, instance=profesor)
        if formularioprofesor.is_valid():
            formularioprofesor.save()
            return redirect('profesores_view')  # Redirige a la vista de lista de profesores después de editar
    else:
        formularioprofesor = ProfesorForm(instance=profesor)
            
    return render(request, 'editar_profesor.html', {'formularioprofesor': formularioprofesor, 'id': profesor.id})




#--------VISTAS CURSOS:

def Cursos(req):
    return render(req, 'Curso.html', {})

#----Vistas busqueda de cursos:

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




#----Vistas Estudiantes:

def Estudiantes(req):
    return render(req, 'Estudiante.html', {})

#----Vistas estudiantes que se registran:

def mensajeestudiantesnuevos(req):
    return render(req, 'mensajeestudiantesnuevos.html', {})

def Registrate(request):
    if request.method == 'POST':
        form = Estudianteformulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mensajeestudiantesnuevos')  # Cambia 'registro_exitoso' al nombre de la vista adecuada
    else:
        form = Estudianteformulario()

    return render(request, 'Registrate.html', {'form': form})


#----Vistas estudiantes, formulario de busqueda:

# def Estudiantesnuevos(request):
#    form = EstudianteSearchForm(request.GET or None)
#    estudiantes = None
#    if form.is_valid():
#         nombre = form.cleaned_data.get('nombre')
#         apellido = form.cleaned_data.get('apellido')
#         casa = form.cleaned_data.get('casa')

#         estudiantes = Estudiante.objects.all()
#         if nombre:
#             estudiantes = estudiantes.filter(nombre__icontains=nombre)
#         if apellido:
#             estudiantes = estudiantes.filter(apellido__icontains=apellido)
#         if casa:
#             estudiantes = estudiantes.filter(casa__nombre__icontains=casa)  # Asumiendo que 'casa' es un ForeignKey relacionado con 'Casa'
#         return render(request, 'resultados_estudiantes.html', {'estudiantes': estudiantes})
   
#    return render(request, 'Estudiantesnuevos.html', {'form': form, 'estudiantes': estudiantes})


#En esta nueva vista podremos abarcar el listado y la busqueda de estudiantes como lo hicimos con los profesores. 

def estudiantes_view(request):
    # Listar todos los estudiantes
    mis_estudiantes = Estudiante.objects.all()

    # Manejar el formulario de búsqueda
    form = EstudianteSearchForm(request.GET or None)
    search_results = None
    if form.is_valid():
        nombre = form.cleaned_data.get('nombre')
        apellido = form.cleaned_data.get('apellido')
        casa = form.cleaned_data.get('casa')

        queryset = Estudiante.objects.all()

        if nombre:
            queryset = queryset.filter(nombre__icontains=nombre)
        if apellido:
            queryset = queryset.filter(apellido__icontains=apellido)
        if casa:
            queryset = queryset.filter(casa__nombre__icontains=casa)

        search_results = queryset

    return render(request, 'Estudiantesnuevos.html', {
        'mis_estudiantes': mis_estudiantes,
        'form': form,
        'search_results': search_results,
    })

#-------Vista de edición estudiantes. 

def editar_estudiante(request, id):
    estudiante = get_object_or_404(Estudiante, id=id)

    if request.method == 'POST':
        formulario_estudiante = Estudianteformulario(request.POST, instance=estudiante)
        if formulario_estudiante.is_valid():
            formulario_estudiante.save()
            return redirect('estudiantes_view')  # Redirige a la vista de lista de estudiantes después de editar
    else:
        formulario_estudiante = Estudianteformulario(instance=estudiante)
            
    return render(request, 'editar_estudiante.html', {'formulario_estudiante': formulario_estudiante, 'id': estudiante.id})

#-------Vista de eliminación estudiantes. 

def eliminar_estudiante(request, id):
    
    estudiante = get_object_or_404(Estudiante, id=id)
    if request.method == 'POST':
        estudiante.delete()
        return redirect('estudiantes_view')
    return render(request, 'eliminar_estudiante.html', {'estudiante': estudiante})


#----Vistas CASAS Magicas:
def Casa(req):
    return render(req, 'Casa.html', {})

#----Vistas Contactenos:

# def Contacto(request):
#     if request.method == 'POST':
#         formulariocontacto = Contactenosformulario(request.POST)
#         if formulariocontacto.is_valid():
#             formulariocontacto.save()
#             return redirect('Home')  # Cambia 'registro_exitoso' al nombre de la vista adecuada
#     else:
#         formulariocontacto = Contactenosformulario()

#     return render(request, 'Contacto.html', {'formulariocontacto': formulariocontacto})


def mensajecontacto(req):
    return render(req, 'mensajecontacto.html')

def Contacto(request):
    if request.method == 'POST':
        formulariocontacto = Contactenosformulario(request.POST)
        if formulariocontacto.is_valid():
            formulariocontacto.save()
            # Enviar correo electrónico
            enviar_correo_contacto(formulariocontacto.cleaned_data)
            return redirect('mensajecontacto')  # Redirige a la página de inicio después de enviar el formulario
    else:
        formulariocontacto = Contactenosformulario()

    return render(request, 'Contacto.html', {'formulariocontacto': formulariocontacto})

def enviar_correo_contacto(data):
    nombre = data['nombre']
    email = data['email']
    asunto = data['asunto']
    mensaje = data['mensaje']

    # Formato del correo electrónico
    subject = f'Nuevo mensaje de contacto: {asunto}'
    message = f'Nombre: {nombre}\nCorreo electrónico: {email}\n\nMensaje:\n{mensaje}'
    from_email = EMAIL_HOST_USER
    to_email = ['luminaracontactenos@gmail.com']  # Dirección de correo donde deseas recibir los mensajes

    # Envío del correo electrónico
    send_mail(subject, message, from_email, to_email)