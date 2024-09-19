from django.contrib import admin
from .models import Usuario, Publicacion, Comentario, Like


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('email', 'nombre_usuario', 'nombres', 'is_staff', 'is_active')
    search_fields = ('email', 'nombre_usuario')
    list_filter = ('is_staff', 'is_active')

admin.site.register(Usuario, UsuarioAdmin)
    

class Publicaciones():
    list_display = ('autor', 'contenido', 'fecha_publicacion')
    search_fields = ('autor', 'fecha_publicacion')
admin.site.register(Publicacion)

admin.site.register(Comentario)

admin.site.register(Like)