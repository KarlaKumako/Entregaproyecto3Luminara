from django import forms
from .models import Estudiante, Casa

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