from django import forms
from .models import *

#class Estudianteformulario(forms.ModelForm):
    #class Meta:
        #model = Estudiante
        #fields = ['nombre', 'apellido', 'email', 'casa', 'habilidad_magica']
        #widgets = {
            #'casa': forms.Select(choices=Casa.CASA_CHOICES),
        #}

class Estudianteformulario(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'email', 'casa', 'habilidad_magica']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'casa': forms.Select(attrs={'class': 'form-select'}),
            'habilidad_magica': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }


class Contactenosformulario(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'email', 'asunto', 'mensaje']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Tu correo electrónico'}),
            'asunto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Asunto'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe tu mensaje aquí', 'rows': 5}),
        }


class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'apellido', 'email', 'profesion', 'Cursos', 'hechizo_favorito', 'criatura_magica']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'profesion': forms.TextInput(attrs={'class': 'form-control'}),
            'Cursos': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'hechizo_favorito': forms.TextInput(attrs={'class': 'form-control'}),
            'criatura_magica': forms.TextInput(attrs={'class': 'form-control'}),
        }
class BusquedaProfesorForm(forms.Form):
    nombre = forms.CharField(required=False, label='Nombre')
    apellido = forms.CharField(required=False, label='Apellido')
    profesion = forms.CharField(required=False, label='Profesión')

class EstudianteSearchForm(forms.Form):
    nombre = forms.CharField(required=False, max_length=30, label='Nombre')
    apellido = forms.CharField(required=False, max_length=30, label='Apellido')
    casa = forms.CharField(required=False, max_length=30, label='Casa') 

#class CursoSearchForm(forms.Form):
    #curso = forms.CharField(label='Curso', required=False)
    #grupos = forms.CharField(label='Grupos', required=False)

#class CursoSearchForm(forms.Form):
    #query = forms.CharField(label='Buscar cursos', required=False)
    #grupo = forms.ModelChoiceField(queryset=Grupos.objects.all(), required=False)

# class CursoSearchForm(forms.Form):
#     curso = forms.CharField(label='Buscar curso', max_length=100)

class BusquedaForm(forms.Form):
    nombre = forms.CharField(required=False, label='Nombre')
    curso = forms.CharField(required=False, label='Curso')

class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupos
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.Select(choices=Grupos.Grupos_CHOICES, attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['Curso', 'Grupos', 'descripcion']
        widgets = {
            'Curso': forms.TextInput(attrs={'class': 'form-control'}),
            'Grupos': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }

class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['titulo', 'contenido']  # Campos que se mostrarán en el formulario de publicación
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }