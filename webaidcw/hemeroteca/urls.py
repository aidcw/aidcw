from django.urls import path
from . import views as hemeroteca_views


urlpatterns = [
    path('hemeroteca/', hemeroteca_views.hemeroteca, name="hemeroteca"),
]
