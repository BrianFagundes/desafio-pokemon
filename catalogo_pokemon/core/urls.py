# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_pokemons, name='lista_pokemons'),
]