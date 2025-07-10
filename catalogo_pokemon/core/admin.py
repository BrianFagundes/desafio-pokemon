# core/admin.py

from django.contrib import admin
from .models import Tipo, Pokemon

@admin.register(Tipo)
class TipoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'tipo_primario', 'tipo_secundario')
    search_fields = ('nome', 'codigo')
    list_filter = ('tipo_primario', 'tipo_secundario')