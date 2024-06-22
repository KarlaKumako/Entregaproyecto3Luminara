Título: Proyecto Luminara

Descripción: La pagina se construye en inspiración al mundo mágico de Harry Potter, en este caso Luminara es una escuela de mágia fundada en Latinoamerica, la pagina cuenta con información intitucional, formularios de inscripción y busqueda. 

1. Información institucional: 
   1.1 Home: Incluye información sobre why us. 
   1.2 Casas: Incluye información sobre los fundadores del mundo magico en latinoamerica representando a cada casa Magica. 
   1.3 Porfesores (Nuestros profesores): Se incluye información sobre los profesores que pertenecen al equipo de Luminara, indicando su perfil y area de especialidad. 
   1.4 Estudiantes(Entorno): Información general sobre el entorno de los estudiantes, celebraciones, y valores, ademas se suman fotos de la comunidad. 
   1.5 Cursos(Explora cursos): Se suma el listado de cursos segun su nucleo, sin embargo los cursos cuentan con niveles y ademas se dictan por grupos, los grupos son los años, primer año, segundo y asi, cada uno tiene un plan de estudios de acuerdo al que pertenece el estudiante. 

2. Formularios de registro:
  2.1 Profesores (Postulate): Se genera un formulario permitiendo a los interesados registrarse como postulantes para perfiles de profesores, se les solicitan datos tales como nombre, apellido, profesión, criatura magica y hechizos, de esta forma se posee un perfil sobre que tipo de materia o curso podria ser al que podria postular,
  2.2 Estudiantes (Registrate): Este formulario permite a los futuros estudiantes generar un registro para ingresar a Luminara, se solicitan algunos campos los cuales incluyen mail, nombre, apellido y casa, esto si proviene ya de otra escuala de magia y posee la misma ya asignada. 
  2.3 Contactanos : Formulario para solicitar información.

3.Formularios de busqueda:
 3.1 Porfesores (Nuestros postulantes): Se permite realizar la busqueda sobre los profesores que se registran como pustulantes para garantizar que los datos fueron cargados, se muestra información básica dejando de lado las aptitudes y talentos de los mismos como información personal. 
 3.2 Estudiantes (Nuevos estudiantes): Se suma información sobre los estudiantes que se registraron previamente, nuevamente con la intención de identificar que eln registro fue correcto. 
 3.2 Cursos (Busca Cursos): Se suma un espacio para identificar de forma mas granular los cursos, a que grupo pertenecen y cuantos modulos posee el mismo. 


 4.Admin:

Se le agrega al admin y a los modelos caracteristicas para permitir una visualización amena y util para filtrar la información, ademas se suman los grupos, los cursos, las casas, para mejorar el entorno de navegación brindandole protegonismo a los formularios correspondientes, en donde por ejemplo se logra dejar un espacio en formato desplegable para el registro de estudiantes donde podran seleccionar asi la casa a la que pertenecen. 

5.Forms: 

Se dejan comentados los forms que se usaron en testeo para lograr algunos formularios, esto para dejar registro de las vias que se intentaron para lograr tal fin. 

6. Models:

Se utilizo en apoyo chat gpt para la creación de los modelos tales como Grupos y Casas, ya que se queria usar los mismos como campos unicos con opciones fijas, por ende se genera en exploración la forma de adecuar el modelo para tal fin evitando que se generen como campos para formularios ya que no son utiles para tal fin. 

Observaciones:

1. Para que sea visible el admin y se pueda visualizar en totalidad:
   User: ProyectoLuminara
   Contraseña: 12345Luminara
Version: 2.5


------------------------------------------------------------------------------------------------------------------------

Nueva versión: 3.0

Profesores: 

Se suma la opción de registro para postulantes solo para usuarios logueados, permitiendo asi tener un control sobre esta información se suma al rol de staff la posibilidad de ver el listado de profesores con la posibilidad de buscar, eliminar o editar a los mismos. 

Estudiantes: 

Se suma al igual que con los profesores la posibilidad de registrar sus datos como postulante a nuevo estudiante, por otro lado se suma la posibilidad de listar por el usuario de staff los estudiantes, eliminarlos o editarlos. 

Cursos:
Debido al tiempo no llegue a realizar el read more mas especifico de acuerdo a cada curso, sin embargo sume una pagina en donde puede ingresar el usuario registrado para verificar los cursos y los grupos de estudiantes de acuerdo al año de cursada. Por otro lado el staff tiene el acceso a modificar o eliminar tantos cursos como erstudiantes. 

Contactanos:

Se genera toda la estructura para generar el contacto en donde llegue por mail el mismo sin embargo por incidencias con google no se logra configurar desde alli la acción, en donde no se logra encontrar la opcion de contraseña para app, debido a esto queda listo para usar pero sin la accion disponible. 

La opcion contraseña de aplicaciones aparece con el factor de dos para el ingreso sin embargo a pesar de seguir todos los pasos de la documentación de google no logre que apareciera la opción para poder unificar este punto. :(

Link de tutorial que se intenta seguir_: https://www.google.com/search?client=opera-gx&q=contactenos+con+django+enviando+mail&sourceid=opera&ie=UTF-8&oe=UTF-8#fpstate=ive&vld=cid:4f0c8b73,vid:3jtMdcvBA3c,st:0

Seguridad: Se genera una segunda APP para todo el dash de usuarios, en donde sumamos la posibilidad del registro, log in, log out,  modificación de perfil, sumar imagenes de avatar, y ademas modificar por separado la contraseña.


NOTA IMPORTANTE: Al generar estos cambios y sumar los decoradores correspondiente sobre el usuario de staff y el logueo del usuario se identifican incidencias con las acciones de eliminar y modificar sobre toda la plataforma, la terminar no arroja errores, verifique la documentación al respecto, busque información pero no encontre casos de uso al respecto, intente sumar ademas puntos de seguridad sobre los templates de los cuales identifico viene el error, ** al accionar cualquiera de los botones desloguea al usuario no permitiendo asi seguir con la gestión*** antes de generar al dash de seguridad se comprobo que todo funcionaba optimo pero al sumarlo paso esto. 