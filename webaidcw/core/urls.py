from django.urls import path
from . import views as core_views


urlpatterns = [
    path('', core_views.inicio, name="inicio"),##no ponemos nada y significa que es el inicio
    path('identidad/', core_views.identidad_social, name="identidad"),
    path('directiva/', core_views.junta_directiva, name="directiva"),
    path('estatutos/', core_views.estatutos_sociales, name="estatutos"),
    path('ayudar/', core_views.ayudar, name="ayudar"),
    path('asociado/', core_views.ayudar_asociado, name="asociado"),
    path('colaborador/', core_views.ayudar_colaborador, name="colaborador"),
    path('donacion/', core_views.ayudar_donar, name="donacion"),
    path('contacto/', core_views.contacto, name="contacto"),
    path('principios/', core_views.principio, name="principios"),
]