from django import forms
from .models import Estudiante, Contacto

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