# core/views.py
from django.shortcuts import render
from .models import Pokemon, Tipo
from django.db.models import Q
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

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

def lista_tipos(request):
    tipos = Tipo.objects.all().order_by('nome')
    contexto = {'tipos': tipos}
    return render(request, 'core/lista_tipos.html', contexto)

class PokemonCreateView(CreateView):
    model = Pokemon
    fields = ['codigo', 'nome', 'tipo_primario', 'tipo_secundario']
    template_name = 'core/pokemon_form.html'
    success_url = reverse_lazy('lista_pokemons')

    def get_initial(self):
        # Pega os valores iniciais da classe pai (se houver)
        initial = super().get_initial()
        
        # Busca o último Pokemon cadastrado, ordenando pelo maior código
        ultimo_pokemon = Pokemon.objects.order_by('-codigo').first()
        
        if ultimo_pokemon:
            # Se existe um, o próximo código é o último + 1
            proximo_codigo = ultimo_pokemon.codigo + 1
        else:
            # Se não existe nenhum, começa do 1
            proximo_codigo = 1
            
        # Define o valor inicial para o campo 'codigo'
        initial['codigo'] = proximo_codigo
        
        return initial

#CRUD para os pokemons

class PokemonUpdateView(UpdateView):
    model = Pokemon
    fields = ['nome', 'tipo_primario', 'tipo_secundario'] # Não permitimos editar o código
    template_name = 'core/pokemon_form.html'
    success_url = reverse_lazy('lista_pokemons')

class PokemonDeleteView(DeleteView):
    model = Pokemon
    template_name = 'core/pokemon_confirmar_delete.html'
    success_url = reverse_lazy('lista_pokemons')

#CRUD para os tipos

class TipoCreateView(CreateView):
    model = Tipo
    fields = ['nome'] # Apenas o campo 'nome' é necessário
    template_name = 'core/tipo_form.html'
    success_url = reverse_lazy('lista_pokemons') # Pode redirecionar para a lista principal

class TipoUpdateView(UpdateView):
    model = Tipo
    fields = ['nome']
    template_name = 'core/tipo_form.html'
    success_url = reverse_lazy('lista_pokemons')

class TipoDeleteView(DeleteView):
    model = Tipo
    template_name = 'core/tipo_confirmar_delete.html'
    success_url = reverse_lazy('lista_pokemons')