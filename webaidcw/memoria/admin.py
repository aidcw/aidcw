from django.contrib import admin
from .models import Memoria # importamos el modelo el .models es para indicarle que es dentro de aqui mismo

# Register your models here.
#Con esto podemos mostrar los campos solo lectura de fecha creacion y fecha modificacion
class MemoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion','fecha_modificacion')
    # mostrar estos campos en el admin de este modelo
    list_display = ('nombre','fecha_memoria',) 
    #buscador para coincidencias en los campos que indiquemos
    search_fields = ('nombre',)
    #Navegar de forma jerarquica por las noticias y su fecha de noticia
    date_hierarchy = 'fecha_memoria'

#debemos registrar nuestros modelos para que salga en el administrador
admin.site.register(Memoria, MemoriaAdmin)
