from django.contrib import admin
from .models import Profesor, Curso, Estudiante, Casa

class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'profesion', 'hechizo_favorito', 'criatura_magica', 'email')

class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'casa', 'habilidad_magica', 'email')

admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Curso)
admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Casa)
