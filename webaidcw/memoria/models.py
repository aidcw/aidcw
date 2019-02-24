from django.db import models
from django.utils.timezone import now

# Create your models here.

class Memoria(models.Model): #Debe ener esta herencia para el ORM
    nombre = models.CharField(max_length=200, verbose_name = "Nombre",  null=True, blank=True)
    fecha_memoria = models.DateTimeField(verbose_name="Fecha de memoria", default=now)
    docuemento = models.FileField(verbose_name="Memoria", upload_to="Memorias") #upload junto con media irá guardando imagenes de cada noticia
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha creación")#Se añadirá la hora automaticamente una sola vez
    fecha_modificacion = models.DateTimeField(auto_now=True, verbose_name = "Fecha modificación")# cada vez que se actualiza
    

    #para que django detecte nombre que queramos
    class Meta:
        verbose_name = "memoria"
        verbose_name_plural = "memorias"
        ordering = ["-fecha_creacion"] 
    
    #para mostrar correctamente las memorias
    def __str__(self):
        return self.nombre