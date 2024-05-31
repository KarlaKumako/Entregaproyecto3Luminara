from django.db import models


class Grupos(models.Model):
    Aprendices_de_las_Estrellas = 'AES'
    Exploradores_de_los_Encantos = 'EXE'
    Guardianes_de_las_Criaturas = 'GCR'
    Alquimistas_del_Bosque = 'ABO'
    Maestros_de_la_Magia = 'MAM'
    
    Grupos_CHOICES = [
        (Aprendices_de_las_Estrellas, 'Aprendices_de_las_Estrellas'),
        (Exploradores_de_los_Encantos, 'Exploradores_de_los_Encantos'),
        (Guardianes_de_las_Criaturas, 'Guardianes_de_las_Criaturas'),
        (Maestros_de_la_Magia, 'Maestros_de_la_Magia'),
    ]
    
    nombre = models.CharField(
        max_length=3,
        choices=Grupos_CHOICES,
        unique=True,
    )
    descripcion = models.TextField()

    def __str__(self):
        return self.get_nombre_display()

    def __str__(self):
        return self.nombre
    

class Curso(models.Model):
    Curso = models.CharField(max_length=100)
    FIELDNAME= models.ManyToManyField(Grupos)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(null=True)
    profesion = models.CharField(max_length=30)
    FIELDNAME= models.ManyToManyField(Curso)
    hechizo_favorito = models.CharField(max_length=100, null=True)  # Nuevo hechizo favorito
    criatura_magica = models.CharField(max_length=100, null=True)  # Criatura mágica favorita

    def __str__(self):
        return f'{self.nombre} {self.apellido} - {self.profesion} {self.email} {self.hechizo_favorito} {self.criatura_magica}'

class Casa(models.Model):
    GRYFFINDOR = 'Gryffindor'
    HUFFLEPUFF = 'Hufflepuff'
    RAVENCLAW = 'Ravenclaw'
    SLYTHERIN = 'Slytherin'
    
    CASA_CHOICES = [
        (GRYFFINDOR, 'Gryffindor'),
        (HUFFLEPUFF, 'Hufflepuff'),
        (RAVENCLAW, 'Ravenclaw'),
        (SLYTHERIN, 'Slytherin'),
    ]
    
    nombre = models.CharField(
        max_length=10,
        choices=CASA_CHOICES,
        unique=True,
    )
    descripcion = models.TextField()

    def __str__(self):
        return self.get_nombre_display()

    def __str__(self):
        return self.nombre

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(null=True)
    casa = models.ForeignKey(Casa, on_delete=models.SET_NULL, null=True)  # Nueva relación con la casa mágica
    habilidad_magica = models.CharField(max_length=100, null=True)  # Nueva habilidad mágica

    def __str__(self):
        return f'{self.nombre} {self.apellido} {self.email} {self.casa}{self.habilidad_magica}'
    

    

    

