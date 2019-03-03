from django.shortcuts import render, get_object_or_404
from .models import Noticia

# Create your views here.


def noticia(request):
    # nos devuelve todos los objetos del modelo
    lista_noticia = Noticia.objects.all()
    return render(request, "noticia/noticias.html", {'noticia': lista_noticia})


def noticia_unica(request, noticia_id):
    """ publi = get_object_or_404(Noticia, id=noticia_id) """
    publicacion = Noticia.objects.filter(id=noticia_id)
    return render(request, "noticia/publicacion.html", {'publicacion': publicacion})

