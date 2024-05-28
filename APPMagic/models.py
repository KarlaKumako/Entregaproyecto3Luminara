from django.db import models


class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(null=True)
    profesion = models.CharField(max_length=30)
    hechizo_favorito = models.CharField(max_length=100, null=True)  # Nuevo hechizo favorito
    criatura_magica = models.CharField(max_length=100, null=True)  # Criatura mágica favorita

    def __str__(self):
        return f'{self.nombre} {self.apellido} - {self.profesion}'

class Casa(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(null=True)
    casa = models.ForeignKey(Casa, on_delete=models.SET_NULL, null=True)  # Nueva relación con la casa mágica
    habilidad_magica = models.CharField(max_length=100, null=True)  # Nueva habilidad mágica

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    
class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    duracion = models.IntegerField()

    def __str__(self):
        return self.nombre
    

