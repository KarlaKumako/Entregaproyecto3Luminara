from django.contrib import admin
from .models import *

class Cursoadmin (admin.ModelAdmin):
    list_display=['Curso','descripcion']
    search_fields=['Curso','Grupos']
    list_filter=['Curso','Grupos']

class Casasadmin (admin.ModelAdmin):
    list_display=['nombre','descripcion']
    search_fields=['nombre']
    list_filter=['nombre']

class Profesoradmin (admin.ModelAdmin):
    list_display=['nombre','apellido', 'profesion', 'email']
    search_fields=['nombre', 'profesion']
    list_filter=['nombre','profesion']

class Estudianteadmin (admin.ModelAdmin):
    list_display=['nombre','apellido','email', 'casa']
    search_fields=['nombre','casa']
    list_filter=['nombre','casa']

class Gruposadmin (admin.ModelAdmin):
    list_display=['nombre','descripcion']
    search_fields=['nombre']
    list_filter=['nombre']

class Contactoadmin (admin.ModelAdmin):
    list_display=['nombre','email', 'asunto']
    search_fields=['nombre','asunto']
    list_filter=['nombre','asunto']



admin.site.register(Curso,Cursoadmin)
admin.site.register(Profesor,Profesoradmin)
admin.site.register(Estudiante,Estudianteadmin)
admin.site.register(Casa,Casasadmin)
admin.site.register(Grupos,Gruposadmin)
admin.site.register(Contacto,Contactoadmin)

