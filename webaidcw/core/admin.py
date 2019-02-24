from django.contrib import admin
from .models import Estatuto # importamos el modelo el .models es para indicarle que es dentro de aqui mismo

# Register your models here.
#Con esto podemos mostrar los campos solo lectura de fecha creacion y fecha modificacion
class EstatutoAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion','fecha_modificacion')

#debemos registrar nuestros modelos para que salga en el administrador
admin.site.register(Estatuto, EstatutoAdmin)
