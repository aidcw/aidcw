from django.db import models
from django.utils.timezone import now
from ckeditor.fields import RichTextField
# Create your models here.

class Hemeroteca(models.Model): #Debe ener esta herencia para el ORM
    titulo = models.CharField(max_length=200, verbose_name = "Título")
    descripcion = RichTextField(verbose_name = "Descripción")
    fecha = models.DateTimeField(verbose_name="Año", default=now)
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha creación")#Se añadirá la hora automaticamente una sola vez
    fecha_modificacion = models.DateTimeField(auto_now=True, verbose_name = "Fecha modificación")# cada vez que se actualiza
    imagen = models.ImageField(verbose_name = "Imagen hemeroteca", upload_to="Hemeroteca") #upload junto con media irá guardando imagenes de cada noticia


    #para que django detecte nombre que queramos
    class Meta:
        verbose_name = "hemeroteca"
        verbose_name_plural = "hemerotecas"
        ordering = ["-fecha_creacion"] #orden de muestra de noticias de más nuevo a mas antiguo
    
    #para mostrar correctamente las noticias
    def __str__(self):
        return self.titulo

