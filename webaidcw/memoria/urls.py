from django.urls import path
from . import views as memoria_views


urlpatterns = [
    path('gestion/', memoria_views.gestion_transparente, name="gestion"),
    path('gestion/<int:memoria_id>/', memoria_views.memoria_unica, name="memoria"),
]