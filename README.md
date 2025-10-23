# Desafio

O seu cliente, Carvalho, é um catalogador de Pokemon. Ele precisa de um sistema para deixar mais fácil o cadastro de novas espécias que ele vem encontrando em suas pesquisas, de forma simples e rápida, através de um sistema web. Carvalho já tem uma lista com 150 desses Pokemons, e o sistema deve vir com esses Pokemons pré-cadastrados.

# Telas

Home

<img width="1904" height="910" alt="image" src="https://github.com/user-attachments/assets/e2c82c46-0096-436b-9544-a874223c8929" />

Gerenciar tipos

<img width="1904" height="908" alt="image" src="https://github.com/user-attachments/assets/7cecac27-ba7c-4397-96b4-e7ce4b6cf225" />

Adicionar tipo

<img width="1914" height="906" alt="image" src="https://github.com/user-attachments/assets/fd300f15-ed2d-4c40-b111-dd81719c6a24" />

Editar tipo

<img width="1917" height="897" alt="image" src="https://github.com/user-attachments/assets/2e4f5006-3e25-4f41-acaa-e7a2d2579d1c" />

Confimação de exclusão (tipo)

<img width="1919" height="911" alt="image" src="https://github.com/user-attachments/assets/57289c04-9629-438a-a296-cb609a622255" />

Adicionar pokémon

<img width="1916" height="905" alt="image" src="https://github.com/user-attachments/assets/b8eaf084-a999-442e-8e7e-7a00012d3870" />

Editar pokémon

<img width="1913" height="899" alt="image" src="https://github.com/user-attachments/assets/ef0213e0-f668-48f5-b865-e74b6c3f11a0" />

Confimação de exclusão (pokémon)

<img width="1916" height="893" alt="image" src="https://github.com/user-attachments/assets/6a60ee66-fee1-4290-ba33-07e6a6ef29cf" />

# Url do video de demonstração

https://youtu.be/1cIypt7pGTc

# Escopo

O desenvolvimento foi estruturado em três versões evolutivas, cada uma em sua própria branch, para demonstrar diferentes abordagens desde uma solução local e simples até uma aplicação conteinerizada e pronta para deploy na nuvem.

# Tecnologias Utilizadas

Backend

Python -> Django

# Frontend

HTML5

Bootstrap 5

# Banco de Dados

SQLite (v1), MySQL (v2, v3)

# DevOps

Docker, Docker Compose

Cloud

AWS (ECR e APP Runner)

# Branch funcionalidade/v1-local-sqlite - Versão local

Objetivo: Criar uma solução funcional e rápida, que não exige nenhuma dependência externa (como Docker) para rodar.

# Branch funcionalidade/v2-dockerizacao - A containerização e utilização do bd MYSQL

Objetivo: Evoluir o projeto para o uso do banco de dados MYSQL e containers, utilizando Docker e Docker Compose.

# Branch release/v3.0

Objetivo: Preparar o proejto para produção (Deploy)

# Como Rodar o Projeto

Siga as instruções abaixo de acordo com a versão que deseja executar.

# Pré-requisitos:

Ter Docker, Docker Compose (V2 e V3), MYSQL(V2 e V3) e Python(V1, V2 e V3) instalados.

# Versão 1: Rodando Localmente

Clone o repositório:

git clone https://github.com/Brian-Moura/desafio-elevential

Instale as depências:

pip install asgiref==3.9.1 Django==5.2.4 numpy==2.3.1 pandas==2.3.1 python-dateutil==2.9.0.post0 pytz==2025.2 six==1.17.0 sqlparse==0.5.3 tzdata==2025.2

Mude para a pasta do projeto:

cd desafio-elevential

Mude para a Branch da primeira versão (v1):

git checkout funcionalidade/v1-local-sqlite

Mude para a pasta do app:

cd catalogo_pokemon

Depois execute o script para iniciar o projeto:

python manage.py runserver

Acesse no navegador, a url:

http://127.0.0.1:8000/

# Versão 2: Rodando com Docker

Clone o repositório:

git clone https://github.com/Brian-Moura/desafio-elevential

Mude para a pasta do projeto:

cd desafio-elevential

Mude para a pasta do app:

cd catalogo_pokemon

Mude para a Branch da segunda versão (v2):

git checkout funcionalidade/v2-dockerizacao

Construa o container:

docker-compose up --build

Acesse no navegador, a url:

http://127.0.0.1:8000/

# Versão 3: Deploy

Acesse a url: https://wivcx82awm.us-east-1.awsapprunner.com - Pausado.
