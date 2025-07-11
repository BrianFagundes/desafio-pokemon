# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # READ 
    path('', views.lista_pokemons, name='lista_pokemons'),
    path('tipos/', views.lista_tipos, name='lista_tipos'),

    #CRUD para os pokemons
    # CREATE
    path('pokemon/adicionar/', views.PokemonCreateView.as_view(), name='pokemon_adicionar'),

    # UPDATE
    path('pokemon/<int:pk>/editar/', views.PokemonUpdateView.as_view(), name='pokemon_editar'),

    # DELETE
    path('pokemon/<int:pk>/deletar/', views.PokemonDeleteView.as_view(), name='pokemon_deletar'),

    #CRUD para os tipos
    # CREATE
    path('tipo/adicionar/', views.TipoCreateView.as_view(), name='tipo_adicionar'),

    # UPDATE
    path('tipo/<int:pk>/editar/', views.TipoUpdateView.as_view(), name='tipo_editar'),

    # DELETE
    path('tipo/<int:pk>/deletar/', views.TipoDeleteView.as_view(), name='tipo_deletar'),
]