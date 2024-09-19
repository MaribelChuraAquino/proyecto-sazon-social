from django.urls import path
from . import views

urlpatterns = [
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('usuarios/crear/', views.crear_usuario, name='crear_usuario'),
    path('usuarios/editar/<int:usuario_id>/', views.editar_usuario, name='editar_usuario'),
    path('usuarios/eliminar/<int:usuario_id>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('registro/', views.registro_usuario, name='registro_usuario'),
    path('login/', views.login_usuario, name='login_usuario'),
    path('publicaciones/', views.like_publicacion, name='lista_publicaciones'),
    path('publicaciones/crear/', views.crear_publicacion, name='crear_publicacion'),
    path('comentarios/<int:comentario_id>/editar/', views.editar_comentario, name='editar_comentario'),
    path('comentarios/<int:comentario_id>/eliminar/', views.eliminar_comentario, name='eliminar_comentario'),
    path('publicaciones/<int:publicacion_id>/comentar/', views.comentar_publicacion, name='comentar_publicacion'),
    path('publicaciones/<int:publicacion_id>/', views.detalle_publicacion, name='detalle_publicacion'),
    path('publicaciones/<int:publicacion_id>/like/', views.like_publicacion, name='like_publicacion'),
    path('perfil/<int:usuario_id>/', views.ver_perfil, name='ver_perfil'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
]
