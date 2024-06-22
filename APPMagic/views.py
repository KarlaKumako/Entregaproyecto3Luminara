from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from Proyecto3Luminara.settings import EMAIL_HOST_USER
from .models import *
from .forms import *
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

"""
Se suman dentro de nuevos conocimientos: 

Manejo de Excepciones: Si el objeto solicitado no existe en la base de datos, get_object_or_404 automáticamente 
genera una respuesta HTTP 404 (Página no encontrada). 
Esto es útil para manejar errores cuando se accede a URLs que corresponden a objetos que no existen.
A pesar de ellos tuve cuidado de brindarle paginas de respuesta antes la falla de registros. 

Tambien se suma la expresión instance esto simplifica mucho el codigo y evita que deba hacer el listado de los datos incluidos
en el modelo. 

Por otro lado cree una vista combinada en dos modelos para incluir los grupos y cursos en un solo lugar.

Se realiza el intento de conectar los comentarios del contactenos con una mailera de gmail, se me presentan inconvenientes desde
la configuración en Google, ya que la contraseña que debe crearse para apps, no me muestra la opción y no logre hacer que aparezca
en la sección de seguridad

"""
def staffmember(req):    
     return render(req, 'staffmember.html',{})

#-------------------VISTA HOME
def home(req):
    return render(req, 'home.html')

#-------------------VISTA PROFESORES

# #----Vistas profesores:

def Profesores(req):    
    return render(req, 'Profesor.html',{})

#----Vistas profesores postulantes:
@staff_member_required(login_url='/APP-Magic/staffmember/')
def Postulantes(req):    
     return render(req, 'Postulantes.html',{})



#----Vista mensaje postulantes:
@login_required()
def mensajepostulado(req):    
     return render(req, 'mensajepostulado.html',{})

# #----Vista formulario postulantes:
@login_required()
def Postulate(request):    
    if request.method == 'POST':
        formularioprofesor = ProfesorForm(request.POST)
        if formularioprofesor.is_valid():
            formularioprofesor.save()
            return redirect('mensajepostulado')  # Redirige a una página de éxito
    else:
        formularioprofesor = ProfesorForm()
    return render(request, 'Postulateformulario.html', {'formularioprofesor': formularioprofesor})

# #----Vista lista/busqueda postulantes:
#Se crea una vista para manejar el formulario de busqueda junto con el listado de profesores. 

@staff_member_required(login_url='/APP-Magic/staffmember/')
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

#-------Vista eliminar profesor:
@staff_member_required(login_url='/APP-Magic/staffmember/')
def eliminar_profesor(request, id):
    profesor = get_object_or_404(Profesor, id=id)

    if request.method == 'POST':
        # Confirmación de la eliminación
        profesor.delete()        
        return redirect('profesores_view')  # Redirige a la vista de lista de profesores

    # Si el método no es POST, renderiza el template de confirmación de eliminación
    return render(request, 'eliminar_profesor.html', {'profesor': profesor})

#----Vista modificación profesor:
@staff_member_required(login_url='/APP-Magic/staffmember/')
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

#----Vista cursos:
def Cursos(req):
    return render(req, 'Curso.html', {})

#----Vista mensaje curso creado:
@staff_member_required(login_url='/APP-Magic/staffmember/')
def mensajecursocreado(req):
    return render(req, 'mensajecursocreado.html', {})

#----Vista creación curso:
@staff_member_required(login_url='/APP-Magic/staffmember/')
def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mensajecursocreado')  # Redirige a una página de éxito o donde desees
    else:
        form = CursoForm()
    
    return render(request, 'crear_curso.html', {'form': form})

#----- VISTA COMPARTIDA DE GRUPOS Y CURSOS
@login_required()
def grupos_y_cursos_view(request):
    # Listar todos los grupos y cursos
    grupos = Grupos.objects.all()
    cursos = Curso.objects.all()

    return render(request, 'Readmorecursos.html', {
        'grupos': grupos,
        'cursos': cursos,
    })

#----Vista eliminación curso:
@staff_member_required(login_url='/APP-Magic/staffmember/')
def eliminar_curso(request, id):

    curso = get_object_or_404(Curso, id=id)
    if request.method == 'POST':        
        curso.delete()
        messages.success(request, f'El curso {curso.Curso} ha sido eliminado correctamente.')
        return redirect('grupos_y_cursos_view') 
    
    return render(request, 'eliminar_curso.html', {'curso': curso})

#----Vista edición curso:
@staff_member_required(login_url='/APP-Magic/staffmember/')
def editar_curso(request, id):

    curso = get_object_or_404(Curso, id=id)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()            
            return redirect('grupos_y_cursos_view')  # Redirige a la vista de lista de cursos después de editar
    else:
        form = CursoForm(instance=curso)
            
    return render(request, 'editar_curso.html', {'form': form, 'id': curso.id})

#-----------------VISTA GRUPOS: 

#-------Vista grupo creado con exito:
@staff_member_required(login_url='/APP-Magic/staffmember/')
def mensajegrupocreado(req):
    return render(req, 'mensajegrupocreado.html', {})

#-------Vista creación de grupos:
@staff_member_required(login_url='/APP-Magic/staffmember/')
def crear_grupo(request):
    if request.method == 'POST':
        form = GrupoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mensajegrupocreado')  # Redirige a una página de éxito o donde desees
    else:
        form = GrupoForm()
    
    return render(request, 'crear_grupo.html', {'form': form})

#-------Vista eliminación de grupos:
@staff_member_required(login_url='/APP-Magic/staffmember/')
def eliminar_grupo(request, id):

    grupo = get_object_or_404(Grupos, id=id)
    if request.method == 'POST':
        grupo.delete()        
        return redirect('grupos_y_cursos_view')  # Redirige a la vista de listado de grupos

    return render(request, 'eliminar_grupo.html', {'grupo': grupo})

#-------Vista edición de grupos:
@staff_member_required(login_url='/APP-Magic/staffmember/')
def editar_grupo(request, id):

    grupo = get_object_or_404(Grupos, id=id)
    if request.method == 'POST':
        form = GrupoForm(request.POST, instance=grupo)
        if form.is_valid():
            form.save()
            # Añadir mensaje de éxito si lo deseas
            return redirect('grupos_y_cursos_view')  # Redirige a la vista de listado de grupos
    else:
        form = GrupoForm(instance=grupo)
    
    return render(request, 'editar_grupo.html', {'form': form, 'grupo': grupo})


#-----------------VISTA ESTUDIANTES: 

#----Vistas Estudiantes:

def Estudiantes(req):
    return render(req, 'Estudiante.html', {})

#----Vistas registro de estudiantes nuevos:

def mensajeestudiantesnuevos(req):
    return render(req, 'mensajeestudiantesnuevos.html', {})


#----Vistas formulario de registro estudiantes:
@login_required()
def Registrate(request):
    if request.method == 'POST':
        form = Estudianteformulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mensajeestudiantesnuevos')  # Cambia 'registro_exitoso' al nombre de la vista adecuada
    else:
        form = Estudianteformulario()

    return render(request, 'Registrate.html', {'form': form})


#En esta nueva vista podremos abarcar el listado y la busqueda de estudiantes como lo hicimos con los profesores. 
@staff_member_required(login_url='/APP-Magic/staffmember/')
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

#-------Vista de edición estudiantes:
@staff_member_required(login_url='/APP-Magic/staffmember/')
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

#-------Vista de eliminación estudiantes:
@staff_member_required(login_url='/APP-Magic/staffmember/')
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

#------------------------------------------------BLOG

# #------------------------PUBLICACIONES

# #----------------Listado de Publicaciones:

# def detalle_publicacion(request, pk):
#     publicacion = get_object_or_404(Publicacion, pk=pk)
#     return render(request, 'detalle_publicacion.html', {'publicacion': publicacion})

# #----------------crear Publicaciones:

# def crear_publicacion(request):
#     if request.method == 'POST':
#         form = PublicacionForm(request.POST)
#         if form.is_valid():
#             nueva_publicacion = form.save(commit=False)
#             nueva_publicacion.autor = request.user  # Asigna el autor actual
#             nueva_publicacion.save()
#             return redirect('detalle_publicacion.html')  # Redirige a la lista de publicaciones
#     else:
#         form = PublicacionForm()
    
#     return render(request, 'crear_publicacion.html', {'form': form})

# #----------------EDITAR Publicacion:

# def editar_publicacion(request, pk):
#     publicacion = get_object_or_404(Publicacion, pk=pk)
    
#     if request.method == 'POST':
#         form = PublicacionForm(request.POST, instance=publicacion)
#         if form.is_valid():
#             form.save()
#             return redirect('detalle_publicacion', pk=publicacion.pk)  # Redirige al detalle de la publicación editada
#     else:
#         form = PublicacionForm(instance=publicacion)
    
#     return render(request, 'editar_publicacion.html', {'form': form, 'publicacion': publicacion})



# #----------------eliminar Publicacion:

# def eliminar_publicacion(request, pk):
#     publicacion = get_object_or_404(Publicacion, pk=pk)
    
#     if request.method == 'POST':
#         publicacion.delete()
#         return redirect('detalle_publicacion')  # Redirige a la lista de publicaciones después de eliminar
    
#     return render(request, 'eliminar_publicacion.html', {'publicacion': publicacion})


# #------------------------COMENTARIOS

# def crear_comentario(request, pk):
#     publicacion = get_object_or_404(Publicacion, pk=pk)
#     if request.method == 'POST':
#         form = ComentarioForm(request.POST)
#         if form.is_valid():
#             comentario = form.save(commit=False)
#             comentario.publicacion = publicacion
#             comentario.autor = request.user
#             comentario.save()
#             return redirect('detalle_publicacion', pk=pk)
#     else:
#         form = ComentarioForm()
#     return render(request, 'crear_comentario.html', {'form': form})

# #----------------editar comentario:

# def editar_comentario(request, pk):
#     comentario = get_object_or_404(Comentario, pk=pk)
#     if request.method == 'POST':
#         form = ComentarioForm(request.POST, instance=comentario)
#         if form.is_valid():
#             form.save()
#             return redirect('detalle_publicacion', pk=comentario.publicacion.pk)
#     else:
#         form = ComentarioForm(instance=comentario)
#     return render(request, 'editar_comentario.html', {'form': form})

# def eliminar_comentario(request, pk):
#     comentario = get_object_or_404(Comentario, pk=pk)
#     if request.method == 'POST':
#         comentario.delete()
#         return redirect('detalle_publicacion', pk=comentario.publicacion.pk)
#     return render(request, 'eliminar_comentario.html', {'comentario': comentario})