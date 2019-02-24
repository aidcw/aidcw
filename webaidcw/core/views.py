from django.shortcuts import render, HttpResponse
from noticia.models import Noticia
from .models import Estatuto

# Create your views here.

""" def inicio(request):
    lista_noticia = Noticia.objects.all() #nos devuelve todos los objetos del modelo
    return render(request, "core/inicio.html", {'noticia':lista_noticia}) # para pasar datos es el tercr parametro con un diccionario
 """
def inicio(request):
    lista_noticia = Noticia.objects.all()
    lista_noticias4 = []
    contador = 0
    #Con este for saco solo 4 de las noticias a buscar y lo envío como diccionarío a la vista
    for i in lista_noticia:
        if contador < 4:
            lista_noticias4.append(i)
            contador +=1
        else:
            break
    return render(request, "core/inicio.html", {'noticia':lista_noticias4}) # para pasar datos es el tercer parametro con un diccionario

def acercade(request):
    return HttpResponse(render(request, "core/acercade.html"))

def identidad_social(request):
    return HttpResponse(render(request, "core/identidad.html"))

def junta_directiva(request):
    return HttpResponse(render(request, "core/directiva.html"))

def estatutos_sociales(request):
    estatuto = Estatuto.objects.all()
    return render(request, "core/estatutos.html", {'estatuto': estatuto})

def ayudar(request):
    return HttpResponse(render(request, "core/ayudar.html"))

def ayudar_asociado(request):
    return HttpResponse(render(request, "core/asociado.html"))

def ayudar_colaborador(request):
    return HttpResponse(render(request, "core/colaborador.html"))

def ayudar_donar(request):
    return HttpResponse(render(request, "core/donacion.html"))

def colaborador(request):
    return HttpResponse(render(request, "core/colaboradores.html"))

def contacto(request):
    return HttpResponse(render(request, "core/contacto.html"))

def principio(request):
    return HttpResponse(render(request, "core/principios.html"))

    

      