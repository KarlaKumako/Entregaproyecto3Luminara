from django.db import models
from django.contrib.auth.models import User


class Grupos(models.Model):
    Aprendices_de_las_Estrellas = 'Aprendices de las Estrellas'
    Exploradores_de_los_Encantos = 'Exploradores de los Encantos'
    Guardianes_de_las_Criaturas = 'Guardianes de las Criaturas'
    Alquimistas_del_Bosque = 'Alquimistas del Bosque'
    Maestros_de_la_Magia = 'Maestros de la Magia'
    
    Grupos_CHOICES = [
        (Aprendices_de_las_Estrellas, '1 año : Aprendices de las Estrellas'),
        (Exploradores_de_los_Encantos, '2 año : Exploradores de los Encantos'),
        (Guardianes_de_las_Criaturas, '3 año :Guardianes de las Criaturas'),
        (Alquimistas_del_Bosque, '4 año : Alquimistas del Bosque'),
        (Maestros_de_la_Magia, '5 año :Maestros de la Magia'),
    ]
    
    nombre = models.CharField(
        max_length=30,
        choices=Grupos_CHOICES,
        unique=True,
    )
    descripcion = models.TextField()

    def __str__(self):
        return self.get_nombre_display()

    def __str__(self):
        return f'{self.nombre}'
    

class Curso(models.Model):
    Curso = models.CharField(max_length=100, unique=True)
    Grupos= models.ManyToManyField(Grupos)
    descripcion = models.TextField()

    def __str__(self):
        return f'{self.Curso} {self.Grupos} {self.descripcion}' 
    
    class Meta():
   
     ordering=('Curso',)
    


class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(null=True)
    profesion = models.CharField(max_length=30)
    Cursos= models.ManyToManyField(Curso)
    hechizo_favorito = models.CharField(max_length=100, null=True)  # Nuevo hechizo favorito
    criatura_magica = models.CharField(max_length=100, null=True)  # Criatura mágica favorita

    def __str__(self):
        return f'{self.nombre} {self.apellido} - {self.profesion} - {self.email} - {self.Cursos}'

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
        return f'{self.nombre} {self.apellido} {self.email} {self.casa}'
    
class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    asunto = models.CharField(max_length=255)
    mensaje = models.TextField()

    def __str__(self):
        return f"{self.asunto} by {self.nombre}"
    

class Publicacion(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='publicaciones')

    def __str__(self):
        return self.titulo   

class Comentario(models.Model):
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario por {self.autor.username} en {self.publicacion.titulo}"