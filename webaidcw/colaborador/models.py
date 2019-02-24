from django.db import models

# Create your models here.


class Colaborador(models.Model): #Debe yener esta herencia para el ORM
    nombre = models.CharField(max_length=200, verbose_name = "Nombre")
    imagen = models.ImageField(verbose_name = "Logo", upload_to="Colaborador", null=True, blank=True) #upload junto con media irá guardando imagenes de cada noticia
                                                                                                      #null y blanck para que no sea obligatorio subir una imagen
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha creación")#Se añadirá la hora automaticamente una sola vez
    fecha_modificacion = models.DateTimeField(auto_now=True, verbose_name = "Fecha modificación")# cada vez que se actualiza

    #para que django detecte nombre que queramos
    class Meta:
        verbose_name = "colaborador"
        verbose_name_plural = "colaboradores"
        ordering = ["-fecha_creacion"] #orden de muestra de noticias de más nuevo a mas antiguo
    
    #para mostrar correctamente las noticias
    def __str__(self):
        return self.nombre