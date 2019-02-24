from django.shortcuts import render
from .models import Colaborador

# Create your views here.

def colaborador(request):
    lista_colaborador = Colaborador.objects.all() #nos devuelve todos los objetos del modelo
    return render(request, "colaborador/colaboradores.html", {'colaborador':lista_colaborador}) # para pasar datos es el tercr parametro con un diccionario