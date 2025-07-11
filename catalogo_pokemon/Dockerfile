# Dockerfile

#Imagem Base
FROM python:3.11-slim

#Variáveis de Ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#Instalação de Dependências do Sistema Operacional 
#Atualiza o gerenciador de pacotes e instala as ferramentas de build
#e as bibliotecas de desenvolvimento do MariaDB/MySQL.
RUN apt-get update && apt-get install -y \
    build-essential \
    pkg-config \
    default-libmysqlclient-dev

#Instalação das Dependências Python
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#Copiar o Código da Aplicação
COPY . .

#Coletar Arquivos Estáticos
RUN python manage.py collectstatic --noinput

#Ponto de Entrada
EXPOSE 10000
CMD ["gunicorn", "catalogo_pokemon.wsgi:application", "--bind", "0.0.0.0:10000"]