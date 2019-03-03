from django.contrib import admin
# importamos el modelo el .models es para indicarle que es dentro de aqui mismo
from .models import Estatuto

# Register your models here.
# Con esto podemos mostrar los campos solo lectura de fecha creacion y fecha modificacion
class EstatutoAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'fecha_modificacion')
    # mostrar estos campos en el admin de este modelo
    list_display = ('nombre', 'fecha_creacion', 'fecha_modificacion')


# debemos registrar nuestros modelos para que salga en el administrador
admin.site.register(Estatuto, EstatutoAdmin)
