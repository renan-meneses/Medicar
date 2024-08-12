# Teste Clinica

Este repositório contém uma aplicação dividida em frontend (Angular) e backend (Django), além de um banco de dados PostgreSQL.

## Estrutura do Projeto

- **frontend/**: Contém a aplicação Angular.
- **backend/**: Contém a aplicação Django.
- **docker-compose.yml**: Orquestra os contêineres Docker para frontend, backend e banco de dados.

## Configuração e Execução

### Requisitos

- Docker
- Docker Compose

### Instruções

1. **Construir e Iniciar os Contêineres**

   Na raiz do projeto, execute:

   ```bash
   docker-compose up --build
	```
	- O backend Django estará disponível em http://localhost:8000.
	- O frontend Angular estará disponível em http://localhost:4200.
	- O banco de dados PostgreSQL estará disponível na porta 5432.
2. ** Configurar Variáveis de Ambiente **
	Certifique-se de que os arquivos .env estejam configurados corretamente para o backend e qualquer outro serviço.

## Deploy 
	Para fazer o deploy do projeto completo:

1. **Crie uma Imagem Docker para o Frontend e Backend:**
	```bash
	cd frontend
	docker build -t meu-frontend-angular .

	cd ../backend
	docker build -t meu-backend-django .

	```
2. **Atualize o Docker Compose se necessário e faça o deploy em um servidor de produção ou serviço de hospedagem que suporte Docker.**
