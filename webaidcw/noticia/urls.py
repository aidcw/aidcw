from django.urls import path
from . import views as noticia_views


urlpatterns = [
    path('noticias/', noticia_views.noticia, name="noticias"),
    path('noticia/<int:noticia_id>/', noticia_views.noticia_unica, name="publicacion"),
]
