# core/views.py
from django.shortcuts import render
from .models import Pokemon, Tipo
from django.db.models import Q

def lista_pokemons(request):
    # Busca inicial de todos os pokemons, ordenados pelo código
    pokemons = Pokemon.objects.all().order_by('codigo')
    tipos = Tipo.objects.all().order_by('nome')

    # Pega os valores dos filtros da URL (se existirem)
    filtro_nome = request.GET.get('nome')
    filtro_tipo = request.GET.get('tipo')

    # Aplica o filtro de nome, se ele foi preenchido
    if filtro_nome:
        pokemons = pokemons.filter(nome__icontains=filtro_nome)

    # Aplica o filtro de tipo, se ele foi selecionado
    if filtro_tipo:
        # Usamos Q objects para fazer uma busca OR (ou no primário OU no secundário)
        pokemons = pokemons.filter(
            Q(tipo_primario__id=filtro_tipo) | Q(tipo_secundario__id=filtro_tipo)
        )

    # Prepara o contexto para enviar os dados para o template
    contexto = {
        'pokemons': pokemons,
        'tipos': tipos
    }
    return render(request, 'core/lista_pokemons.html', contexto)