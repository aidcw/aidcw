"""webaidcw URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    # Paths del core
    path('', include('core.urls')),
    # Paths de colaboradores
    path('', include('colaborador.urls')),
    # Paths de noticias
    path('', include('noticia.urls')),
    # Paths de memorias
    path('', include('memoria.urls')),
    # Paths de hemeroteca
    path('', include('hemeroteca.urls')),
    # Paths de admin
    path('admin/', admin.site.urls),  # se cambiará al final por seguridad
]

# para servir ficheros estaticos es decir imagenes en este caso, solo en modo debug
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


#CUSTOM TITLES FOR ADMIN
admin.site.site_header = "Administrar AIDCW"
admin.site.index_title = "Panel de administrador"
admin.site.site_title = "AIDCW"