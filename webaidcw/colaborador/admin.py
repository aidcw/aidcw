from django.contrib import admin
from .models import Colaborador

# Register your models here.
# Con esto podemos mostrar los campos solo lectura de fecha creacion y fecha modificacion
class ColaboradorAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'fecha_modificacion')
    # mostrar estos campos en el admin de este modelo
    list_display = ('nombre', 'fecha_creacion')
    # buscador para coincidencias en los campos que indiquemos
    search_fields = ('nombre',)


# debemos registrar nuestros modelos para que salga en el administrador
admin.site.register(Colaborador, ColaboradorAdmin)
