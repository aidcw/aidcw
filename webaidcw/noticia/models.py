from django.db import models
from django.utils.timezone import now
#para poder usar texto enriquecido
from ckeditor.fields import RichTextField
# Create your models here.

class Noticia(models.Model): #Debe ener esta herencia para el ORM
    titulo = models.CharField(max_length=200, verbose_name = "Título")
    descripcion = RichTextField(verbose_name = "Descripción")
    fecha_noticia = models.DateTimeField(verbose_name="Fecha de noticia", default=now)
    localizacion = models.CharField(max_length=20, verbose_name= "Localización", null=True, blank=True, default="-")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha creación")#Se añadirá la hora automaticamente una sola vez
    fecha_modificacion = models.DateTimeField(auto_now=True, verbose_name = "Fecha modificación")# cada vez que se actualiza
    imagen = models.ImageField(verbose_name = "Imagen Noticia", upload_to="Noticia") #upload junto con media irá guardando imagenes de cada noticia


    #para que django detecte nombre que queramos
    class Meta:
        verbose_name = "noticia"
        verbose_name_plural = "noticias"
        ordering = ["-fecha_creacion"] #orden de muestra de noticias de más nuevo a mas antiguo
    
    #para mostrar correctamente las noticias
    def __str__(self):
        return self.titulo

