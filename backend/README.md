# Backend - Medicar

Este repositório contém o backend da aplicação, desenvolvido com Django.

## Requisitos

- Python 3.11
- pip

## Configuração

1. **Instalar Dependências**

   ```bash
   pip install -r requirements.txt
    ```
2. **Configurar Variáveis de Ambiente**
    ```env

    SECRET_KEY="django-insecure-uw_!=t%xo2om(vn%i*$znf5niv4%5skwn9)l0#&knle2az6dgp"
    DEBUG=TRUE
    EXPIRE_TOKEN=20 
    EXPIRE_REFRESH_TOKEN=60 

    ALLOWED_HOSTS=['localhost', '127.0.0.1']
    #DB SETTINGS
    DB_NAME=
    DB_USER=
    DB_PASSWORD=
    DB_HOST=
    DB_PORT=

    #EMAIL SETTINGS
    EMAIL_HOST=""
    EMAIL_HOST_USER=""
    EMAIL_HOST_PASSWORD=""
    EMAIL_PORT=""
    DEFAULT_FROM_EMAIL="admin@medicar.com"
    ```
3. **Executar Migrações**
     ```bash
        python manage.py migrate
     ```
4. **Rodar o Servidor de Desenvolvimento**
    ```bash
        python manage.py runserver
    ```
    O backend estará disponível em http://localhost:8000.

## Docker
Para construir e rodar o backend com Docker:

1. **Construir a Imagem Docker**
    ```bash
    docker build -t meu-backend-django .
    ```
2. **Rodar o Contêiner**
    ```bash
    docker run -p 8000:8000 --env-file .env meu-backend-django

    ```
O backend estará disponível em http://localhost:8000.


#### Requisição

```
GET /consultas/
```

#### Retorno

```json
[
  {
    "id": 1,
    "dia": "2022-02-05",
    "horario": "12:00",
    "data_agendamento": "2022-02-01T10:45:0-03:00",
    "medico": {
      "id": 1,
      "crm": 3711,
      "nome": "Drauzio Varella",
      "email": "drauzinho@globo.com"
    }
  },
  {
    "id": 2,
    "dia": "2022-03-01",
    "horario": "09:00",
    "data_agendamento": "2022-02-01T10:45:0-03:00",
    "medico": {
      "id": 2,
      "crm": 2544,
      "nome": "Gregory House",
      "email": "greg@hbo.com.br"
    }
  }
]
```

#### Regras de negócio

- A listagem não deve exibir consultas para dia e horário passados
- Os itens da listagem devem vir ordenados por ordem crescente do dia e horário da consulta

### Listar agendas disponíveis

Lista todas as agendas disponíveis na clínica

```json
[
  {
    "id": 1,
    "medico": {
      "id": 1,
      "crm": 3711,
      "nome": "Drauzio Varella",
      "email": "drauzinho@globo.com"
    },
    "dia": "2020-02-10",
    "horarios": ["14:00", "14:15", "16:00"]
  },
  {
    "id": 2,
    "medico": {
      "id": 2,
      "crm": 2544,
      "nome": "Gregory House",
      "email": "greg@hbo.com.br"
    },
    "dia": "2020-02-10",
    "horarios": ["08:00", "08:30", "09:00", "09:30", "14:00"]
  }
]
```

#### Filtros

- Identificador de um ou mais médicos
- Identificador de uma ou mais CRM
- Intervalo de data

```
# Retorna as agendas dos médicos 1 e 2 no período de 1 a 5 de janeiro
GET /agendas/?medico=1&medico=2&data_inicio=2022-01-01&data_final=2022-01-05

# Retorna as agendas dos médicos de CRM passados no filtro no período de 1 a 5 de janeiro
GET /agendas/?crm=2544&crm=3711&data_inicio=2022-01-01&data_final=2022-01-05
```

#### Regras de negócio

- As agendas devem vir ordenadas por ordem crescente de data
- Agendas para datas passadas ou que todos os seus horários já foram preenchidos devem ser excluídas da listagem
- Horários dentro de uma agenda que já passaram ou que foram preenchidos devem ser excluídos da listagem

### Marcar consulta

Marca uma consulta

#### Requisição

```
POST /consultas/
{
  "agenda_id": 1,
  "horario": "14:15"
}
```

#### Retorno

```json
{
  "id": 2,
  "dia": "2022-03-01",
  "horario": "09:00",
  "data_agendamento": "2022-02-01T10:45:0-03:00",
  "medico": {
    "id": 1,
    "crm": 3711,
    "nome": "Drauzio Varella",
    "email": "drauzinho@globo.com"
  }
}
```

#### Regras de negócio

- A data em que o agendamento foi feito deve ser salva ao se marcar uma consulta
- Não deve ser possível marcar uma consulta para um dia e horário passados
- Não deve ser possível marcar uma consulta se o dia e horário já foram preenchidos

### Desmarcar consulta

Desmarca uma consulta

#### Requisição

```
DELETE /consultas/<consulta_id>
```