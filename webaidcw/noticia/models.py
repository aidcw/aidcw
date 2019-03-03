from django.db import models
from django.utils.timezone import now
#para poder usar texto enriquecido
from ckeditor.fields import RichTextField
# Create your models here.
    
class Album(models.Model):
    titulo = models.CharField(max_length=200, verbose_name = "Título")
    imagen1 = models.ImageField(verbose_name = "Imagen principal", upload_to="Noticia")
    imagen2 = models.ImageField(verbose_name = "Imagen 2", upload_to="Noticia", null=True, blank=True)
    imagen3 = models.ImageField(verbose_name = "Imagen 3", upload_to="Noticia", null=True, blank=True)
    imagen4 = models.ImageField(verbose_name = "Imagen 4", upload_to="Noticia", null=True, blank=True)
    imagen5 = models.ImageField(verbose_name = "Imagen 5", upload_to="Noticia", null=True, blank=True)
    imagen6 = models.ImageField(verbose_name = "Imagen 6", upload_to="Noticia", null=True, blank=True)
    imagen7 = models.ImageField(verbose_name = "Imagen 7", upload_to="Noticia", null=True, blank=True)
    imagen8 = models.ImageField(verbose_name = "Imagen 8", upload_to="Noticia", null=True, blank=True)
    imagen9 = models.ImageField(verbose_name = "Imagen 9", upload_to="Noticia", null=True, blank=True)
    imagen10 = models.ImageField(verbose_name = "Imagen 10", upload_to="Noticia", null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha creación")#Se añadirá la hora automaticamente una sola vez
    fecha_modificacion = models.DateTimeField(auto_now=True, verbose_name = "Fecha modificación")# cada vez que se actualiza

    #para que django detecte nombre que queramos
    class Meta:
        verbose_name = "imagen para la noticia"
        verbose_name_plural = "imagenes para las noticias"
        ordering = ["-fecha_creacion"] 
    
   
    def __str__(self):
        return self.titulo



class Noticia(models.Model): #Debe ener esta herencia para el ORM
    titulo = models.CharField(max_length=200, verbose_name = "Título")
    descripcion = RichTextField(verbose_name = "Descripción")
    fecha_noticia = models.DateTimeField(verbose_name="Fecha de noticia", default=now)
    localizacion = models.CharField(max_length=20, verbose_name= "Localización", null=True, blank=True, default="-")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha creación")#Se añadirá la hora automaticamente una sola vez
    fecha_modificacion = models.DateTimeField(auto_now=True, verbose_name = "Fecha modificación")# cada vez que se actualiza
    album = models.ForeignKey(Album, related_name='images', on_delete=models.PROTECT)

    #para que django detecte nombre que queramos
    class Meta:
        verbose_name = "noticia"
        verbose_name_plural = "noticias"
        ordering = ["-fecha_creacion"] #orden de muestra de noticias de más nuevo a mas antiguo
    
    #para mostrar correctamente las noticias
    def __str__(self):
        return self.titulo


