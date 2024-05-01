# FICHAMED API — Django Rest Framework

### Descrição / Description

> [PT-BR]

Esta API oferece autenticação por JWT (Bearer Token) e funcionalidades completas de gestão de Usuários e gestão de Fichas de Atendimento Médico.

Considere executar as primeiras requisições com pelo menos com 1 superuser já inserido no Banco de Dados para gerar o Token.

**NOTA:** Se preferir, modifique a variável ***DEVELOPMENT_MODE*** para ***True*** e utilize o SQLite3 como Banco de Dados em Desenvolvimento.

##

> [EN-US]

This API provides JWT (Bearer Token) authentication and full functionalities for user management and management of Medical Attendance Records.

Consider making the initial requests with at least 1 superuser already inserted into the Database to generate the Token.

**NOTE:**
If preferred, set the ***DEVELOPMENT_MODE*** variable to ***True*** and use SQLite3 as the Development Database.

## Documentação da API / API Documentation

* [Postman]()


# Instalação / Installation

### Criando Banco de Dados / Create Database

> [PT-BR]

As etapas abaixo consideram um BD PostgreSQL executando num container Docker, mas você pode utilizar outro ambiente de sua preferência.

##

> [EN-US]

The step-by-step below assumes a PostgreSQL database running in a Docker container, but you can use another environment of your choice.

## PostgreSQL Docker
> [PT-BR] NOTA: Se preferir, ajuste os valores das variáveis do arquivo Dockerfile de acordo com a sua preferência

> [EN-US] NOTE: If preferred, adjust the values of the variables in the Dockerfile according to your preference.

```bash
  cd fichamed-api
  docker docker build -t db_ps_fichamed .
  docker run --name container_db_ps_fichamed -d -p 5433:5432 db_ps_fichamed
```

##

### Preparando ambiente Python / Preparing Python Environment

* [PT-BR] Criando Ambiente Virtual da API
* [EN-US] Creating Virtual Environment for the API
```bash
  cd fichamed-api
  python -m venv venv
  cd venv/scripts
  .\activate
  cd ../..
```

##

* [PT-BR] Instalando dependências
* [EN-US] Installing dependencies
```bash
  pip install -r requirements.txt
  pip install -r requirements-dev.txt
```
##

> * [PT-BR] Renomei o arquivo **.env.example** para **.env** e ajuste os valores das variáveis de ambiente, se necessário.
> * [EN-US] Rename the file **.env.example** to **.env** and adjust the values of the environment variables, if necessary.

##

* [PT-BR] Executando API Server
* [EN-US] Running API Server
```bash
  python manage.py runserver
```

## Stack utilizada / used

### Back-end:
* Python Django Rest Framework
* PostgreSQL
* Docker
