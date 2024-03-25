# Mooney Python Flask API

## Objetivo

Projeto destinado a estudos e testes, por isso sempre estara em constantes mudanças.
Consumo API Rest para :
    Autenticação JWT,
    Autenticação OAuth2,
    Treinamento de Inteligencia Artificial e testes relacionados.

## Tecnologias Utilizadas

- Python
- Flask
- Docker
- API REST

## Conceitos Trabalhados

- API REST

## Estrutura de Arquivos e Pastas

```
├── mooney-flask/
│   ├── app/
│   │   ├── classification/
│   │   │   └── blueprint.py
│   │   │   └── __init__.py
│   │   │   ├── __pycache__/
│   │   │   │   └── blueprint.cpython-39.pyc
│   │   │   │   └── __init__.cpython-39.pyc
│   │   │   │   └── routes.cpython-39.pyc
│   │   │   └── routes.py
│   │   └── extensions.py
│   │   └── __init__.py
│   │   ├── __pycache__/
│   │   │   └── extensions.cpython-39.pyc
│   │   │   └── __init__.cpython-39.pyc
│   │   │   └── routes.cpython-39.pyc
│   │   └── routes.py
│   │   ├── user/
│   │   │   └── auth.py
│   │   │   └── blueprint.py
│   │   │   └── __init__.py
│   │   │   └── models.py
│   │   │   ├── __pycache__/
│   │   │   │   └── blueprint.cpython-39.pyc
│   │   │   │   └── extensions.cpython-39.pyc
│   │   │   │   └── __init__.cpython-39.pyc
│   │   │   │   └── models.cpython-39.pyc
│   │   │   │   └── routes.cpython-39.pyc
│   │   │   └── routes.py
│   ├── app copy/
│   │   ├── classification/
│   │   │   └── blueprint.py
│   │   │   └── __init__.py
│   │   │   ├── __pycache__/
│   │   │   │   └── blueprint.cpython-39.pyc
│   │   │   │   └── __init__.cpython-39.pyc
│   │   │   │   └── routes.cpython-39.pyc
│   │   │   └── routes.py
│   │   └── extensions.py
│   │   └── __init__.py
│   │   ├── __pycache__/
│   │   │   └── extensions.cpython-39.pyc
│   │   │   └── __init__.cpython-39.pyc
│   │   │   └── routes.cpython-39.pyc
│   │   └── routes.py
│   │   ├── user/
│   │   │   └── auth.py
│   │   │   └── blueprint.py
│   │   │   └── __init__.py
│   │   │   └── models.py
│   │   │   ├── __pycache__/
│   │   │   │   └── blueprint.cpython-39.pyc
│   │   │   │   └── extensions.cpython-39.pyc
│   │   │   │   └── __init__.cpython-39.pyc
│   │   │   │   └── models.cpython-39.pyc
│   │   │   │   └── routes.cpython-39.pyc
│   │   │   └── routes.py
│   └── docker-compose.yml
│   └── Dockerfile
│   └── draw_tree.sh
│   ├── migrations/
│   │   └── alembic.ini
│   │   └── env.py
│   │   ├── __pycache__/
│   │   │   └── env.cpython-39.pyc
│   │   └── README
│   │   └── script.py.mako
│   │   ├── versions/
│   │   │   └── a955de4e44db_migrate_inicial.py
│   │   │   └── fd067491c1f4_user.py
│   │   │   ├── __pycache__/
│   │   │   │   └── a955de4e44db_migrate_inicial.cpython-39.pyc
│   │   │   │   └── fd067491c1f4_user.cpython-39.pyc
│   └── requirements.txt
│   └── structure.txt

```

## Passos para Executar o Projeto Localmente

### Pré-requisitos

- Git
- Python
- Pip
- Docker
- Docker Compose

### Ambiente de Testes

- Recomendado: Ubuntu

### Clonar o Repositório

```bash
git clone git@github.com:daniloftorres/mooney-flask.git .
```

### Executar com Docker Compose

```bash
docker-compose -f docker-compose.local.yml up
```

Devera ver algo parecido com isso

```bash

```

São 3 serviços principais rodando:

- Flask

- Postgres

### Migrations iniciais.

Adicione no arquivo hosts as configurações abaixo:

```bash
docker exec -it mooney-flask python flask migrate
```

```bash
docker exec -it mooney-flask python flask upgrade
```

# API

Este documento fornece instruções sobre como acessar e interagir com a Mooney Flask API. Abaixo estão listados os endpoints disponíveis e exemplos de como fazer requisições para cada um deles.

## Autenticação JWT

Para acessar a maioria dos endpoints, é necessário obter um token JWT e incluí-lo no cabeçalho das suas requisições.

### Obter Token JWT

```bash
curl --location --request POST 'http://api.mooney.com/v1/token/' \
--header 'Content-Type: application/json' \
--data-raw '{
"username": "mooney",
"password": "mooney"
}'
```

### Refresh Token JWT

```bash
curl --location --request POST 'http://api.mooney.com/v1/token/refresh/' \
--header 'Content-Type: application/json' \
--data-raw '{
"refresh": "{{refresh_token}}"
}
'
```

## Autenticação OAuth2

### Obter Token via Client Credentials

```bash
curl --location --request POST 'http://api.mooney.com/v1/oauth2/token/' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'client_id=76rpCwJqi34TCtR5euRlixQWBFfmt0zXYLvmYWDr' \
--data-urlencode 'client_secret=z63fKkzs9e3Ux22KlhnGvQNSYz1IIjdGr5OgIW228ZAmmebJckKyJPOzix4PfygE1VYrvf68KrT5BgqPyhPWolytvrcrSzXomXqgHA8u6xhILjwdqVHirPdMqVQESUCT' \
--data-urlencode 'grant_type=client_credentials'
```
## Postman

Algumas configuração para quem usa Postman como programa para testar as API, mas o conceito serve para quase todos no mesmo genero:

- [Configuração básica para uso do Postman](documentation/postman/var-enviroment.md)

1. Criar Variaveis de Ambiente.
2. Configurar script para quando o request de obtenção do token tiver retorno, capturar o token para savar em nossa variavel de ambiente.
3. Adicionar a variavel de ambiente nas requests dentro do Authozitation : Bearer Token