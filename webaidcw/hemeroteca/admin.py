from django.contrib import admin
from .models import Hemeroteca

# Register your models here.
# Con esto podemos mostrar los campos solo lectura de fecha creacion y fecha modificacion
class HemerotecaAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'fecha_modificacion')
    # mostrar estos campos en el admin de este modelo
    list_display = ('titulo', 'fecha', 'fecha_creacion')
    # buscador para coincidencias en los campos que indiquemos
    search_fields = ('titulo', )
    # Navegar de forma jerarquica por las noticias y su fecha de noticia
    date_hierarchy = 'fecha'


# debemos registrar nuestros modelos para que salga en el administrador
admin.site.register(Hemeroteca, HemerotecaAdmin)
