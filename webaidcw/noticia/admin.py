from django.contrib import admin
from .models import Noticia, Album

# Register your models here.
#Con esto podemos mostrar los campos solo lectura de fecha creacion y fecha modificacion
class NoticiaAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion','fecha_modificacion')
    # mostrar estos campos en el admin de este modelo
    list_display = ('titulo','fecha_noticia','localizacion', 'fecha_creacion') 
    #buscador para coincidencias en los campos que indiquemos
    search_fields = ('titulo', 'localizacion', )
    #Navegar de forma jerarquica por las noticias y su fecha de noticia
    date_hierarchy = 'fecha_noticia'


class AlbumAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion','fecha_modificacion')

#debemos registrar nuestros modelos para que salga en el administrador
admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Album, AlbumAdmin)

