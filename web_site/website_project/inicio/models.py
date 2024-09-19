# Importa las clases y funciones necesarias para crear un usuario personalizado en Django
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Importa los signals para responder a eventos como la creación y actualización de instancias de modelos
from django.db.models.signals import post_save
# Importa el receptor de señales para ejecutar funciones en respuesta a eventos
from django.dispatch import receiver
# Importa la configuración de ajustes del proyecto
from django.conf import settings
# Importa las herramientas para definir modelos de datos en Django
from django.db import models

# Manager para el modelo Usuario
class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        # Verifica si se proporciona un email
        if not email:
            raise ValueError('El email es obligatorio')
        email = self.normalize_email(email)  # Normaliza el email (minúsculas)
        user = self.model(email=email, **extra_fields)  # Crea la instancia de usuario
        user.set_password(password)  # Encripta la contraseña
        user.save(using=self._db)  # Guarda el usuario en la base de datos
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        # Configura los campos adicionales para el superusuario
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)  # Crea el superusuario

# Modelo personalizado para el usuario
class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)  # Email único para el usuario
    nombres = models.CharField(max_length=100)  # Nombres del usuario
    nombre_usuario = models.CharField(max_length=100, unique=True)  # Nombre de usuario único
    is_staff = models.BooleanField(default=False)  # Permite acceso al admin
    is_active = models.BooleanField(default=True)  # Marca si el usuario está activo
    last_login = models.DateTimeField(null=True, blank=True)  # Fecha del último inicio de sesión

    # Relación ManyToMany con los grupos de permisos
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='%(class)s_set',  # `related_name` único para este modelo
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    
    # Relación ManyToMany con permisos específicos del usuario
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='%(class)s_permissions',  # `related_name` único para este modelo
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    objects = UsuarioManager()  # Asigna el manager personalizado

    USERNAME_FIELD = 'email'  # Campo utilizado para el inicio de sesión
    REQUIRED_FIELDS = ['nombres', 'nombre_usuario']  # Campos requeridos al crear un superusuario

    def __str__(self):
        return self.email  # Representación del objeto en forma de string
    
# Modelo para las publicaciones
class Publicacion(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Usuario autor de la publicación
    contenido = models.TextField()  # Contenido de la publicación
    fecha_publicacion = models.DateTimeField(auto_now_add=True)  # Fecha en que se creó la publicación
    imagen = models.ImageField(upload_to='publicaciones/', blank=True, null=True)  # Imagen opcional en la publicación
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='publicaciones_liked', blank=True)
    
    def __str__(self):
        return self.contenido[:50]  # Muestra los primeros 50 caracteres del contenido
    
# Modelo para los comentarios en las publicaciones
class Comentario(models.Model):
    publicacion = models.ForeignKey(Publicacion, related_name='comentarios', on_delete=models.CASCADE)  # Publicación a la que pertenece el comentario
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Usuario que hizo el comentario
    contenido = models.TextField()  # Contenido del comentario
    fecha_comentario = models.DateTimeField(auto_now_add=True)  # Fecha en que se creó el comentario

    def __str__(self):
        return f'{self.autor.nombre_usuario} - {self.fecha_comentario}'  # Representación del comentario
    
# Modelo para los 'likes' en las publicaciones
class Like(models.Model):
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)  # Publicación a la que se le da 'me gusta'
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Usuario que dio 'me gusta'
    fecha_like = models.DateTimeField(auto_now_add=True)  # Fecha en que se dio el 'me gusta'

# Modelo para el perfil del usuario
class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Usuario asociado al perfil
    biografia = models.TextField(blank=True, null=True)  # Biografía opcional del usuario
    foto_perfil = models.ImageField(upload_to='perfil/', blank=True, null=True)  # Imagen de perfil opcional

    def __str__(self):
        return self.usuario.nombre_usuario  # Representación del perfil en forma de string
    
# Señal para crear un perfil de usuario cuando se crea un nuevo usuario
@receiver(post_save, sender=Usuario)
def crear_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        PerfilUsuario.objects.create(usuario=instance)

# Señal para guardar el perfil del usuario cuando se guarda el usuario
@receiver(post_save, sender=Usuario)
def guardar_perfil_usuario(sender, instance, **kwargs):
    instance.perfilusuario.save()
