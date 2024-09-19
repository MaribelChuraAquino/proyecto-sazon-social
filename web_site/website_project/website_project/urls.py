"""
URL configuration for website_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', include('inicio.urls')),
]

# Si el entorno de desarrollo está habilitado (es decir, DEBUG=True en settings.py)
if settings.DEBUG:
    # Añade una URL de acceso estático para servir archivos de medios durante el desarrollo
    # `settings.MEDIA_URL` es la URL desde la que se sirven los archivos de medios
    # `settings.MEDIA_ROOT` es la ubicación en el sistema de archivos donde se almacenan los archivos de medios
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)