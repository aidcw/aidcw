from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Memoria
# Create your views here.


def gestion_transparente(request):
    lista_memoria = Memoria.objects.all()
    return render(request, "memoria/gestion.html", {'memoria':lista_memoria})


def memoria_unica(request, memoria_id):
    mem = get_object_or_404(Memoria,id=memoria_id)
    memoria = Memoria.objects.filter(id = mem.id)
    return render(request, "memoria/gestion.html", {'memoria': memoria})