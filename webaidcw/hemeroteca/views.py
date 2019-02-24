from django.shortcuts import render, get_object_or_404
from .models import Hemeroteca


# Create your views here.

def hemeroteca(request):
    # nos devuelve todos los objetos del modelo
    hemeroteca = Hemeroteca.objects.all()
    # para pasar datos es el tercr parametro con un diccionario
    return render(request, "hemeroteca/hemeroteca.html", {'hemeroteca': hemeroteca})
