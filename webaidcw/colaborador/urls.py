from django.urls import path
from . import views as colaborador_views


urlpatterns = [
    # Paths de colaboradores
    path('colaboradores/', colaborador_views.colaborador, name="colaboradores"),
]
