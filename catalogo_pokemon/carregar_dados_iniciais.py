# carregar_dados_iniciais.py
import os
import django
import pandas as pd

# Configura o ambiente do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'catalogo_pokemon.settings')
django.setup()

from core.models import Tipo, Pokemon

def carregar_dados():
    print("Iniciando o carregamento de dados...")

    # Limpa dados antigos
    Pokemon.objects.all().delete()
    Tipo.objects.all().delete()
    print("Modelos antigos deletados.")

    #Leitura direta do JSON para o DataFrame do pandas
    df = pd.read_json('dados_iniciais.json')

    #Lógica para extrair todos os tipos únicos
    tipos_primarios = set(df['tipo_primario'].dropna())
    tipos_secundarios = set(df['tipo_secundario'].dropna())
    todos_os_tipos = tipos_primarios.union(tipos_secundarios)

    for nome_tipo in todos_os_tipos:
        Tipo.objects.get_or_create(nome=nome_tipo)
    print(f"{len(todos_os_tipos)} tipos foram criados.")

    # Cria os Pokemons
    for indice, linha in df.iterrows():
        #Acessando as colunas 'tipo_primario' e 'tipo_secundario'
        tipo_primario_obj = Tipo.objects.get(nome=linha['tipo_primario'])

        tipo_secundario_obj = None
        # pd.notna verifica se o valor não é nulo/NaN
        if pd.notna(linha['tipo_secundario']):
            tipo_secundario_obj = Tipo.objects.get(nome=linha['tipo_secundario'])

        Pokemon.objects.create(
            codigo=int(linha['codigo']),
            nome=linha['nome'],
            tipo_primario=tipo_primario_obj,
            tipo_secundario=tipo_secundario_obj
        )
    print(f"{len(df)} Pokemons foram criados.")
    print("Carregamento de dados concluído com sucesso!")

if __name__ == '__main__':
    carregar_dados()