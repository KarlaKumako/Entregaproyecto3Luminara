from django.contrib import admin
from .models import Profesor, Curso, Estudiante, Casa, Grupos

admin.site.register(Profesor)
admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(Casa)
admin.site.register(Grupos)