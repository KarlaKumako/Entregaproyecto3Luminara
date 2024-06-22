
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import *
from django.contrib.auth.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User

#------------------VISTA LOGIN

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)            
                return redirect('Home')  
            else:
                # Usuario no válido
                form.add_error(None, 'Nombre de usuario o contraseña incorrectos.')
    else:
        form = CustomAuthenticationForm()

    return render(request, 'login.html', {'form': form})


#------------------VISTA REGISTRO

#----Vistas mensaje registro exitoso:

def registroexitoso(req):
    return render(req, 'registroexitoso.html', {})

#-----formularo de registro:

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Autentica y conecta automáticamente al usuario
            return redirect('registroexitoso')  # Redirige a la página de inicio después del registro
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})


#-----Perfil/ modificación de avatar: 
@login_required
def perfil(request):
    try:
        avatar = Avatar.objects.get(user=request.user)
    except Avatar.DoesNotExist:
        avatar = None

    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES, instance=avatar)
        if form.is_valid():
            avatar_instance = form.save(commit=False)
            avatar_instance.user = request.user
            avatar_instance.save()
            return redirect('perfil')  # Redireccionar a la página de perfil después de guardar el avatar
    else:
        form = AvatarForm(instance=avatar)

    return render(request, 'perfil.html', {'avatar': avatar, 'form': form})




#-----Modificación de datos de registro:

@login_required()
def editar_perfil(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('perfil')  
    else:
        form = CustomUserForm(instance=request.user)
    
    return render(request, 'editar_perfil.html', {'form': form})


#-----Modificación de contraseña:

@login_required()
def cambiar_contraseña(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Mantiene al usuario logueado después de cambiar la contraseña
            messages.success(request, 'Tu contraseña ha sido actualizada exitosamente.')
            return redirect('perfil')
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'cambiar_contraseña.html', {'form': form})
