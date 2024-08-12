# Frontend - Medicar

Este repositório contém o frontend da aplicação, desenvolvido com Angular.

## Requisitos

- Node.js 18.x ou superior
- npm (ou Yarn)

## Configuração

1. **Instalar Dependências**

    ```bash
    npm install
    ```

2. **Rodar o Servidor de Desenvolvimento**
    ```bash
    npm start
    ```
    O aplicativo estará disponível em http://localhost:4200.

## Construção

Para criar uma versão de produção do aplicativo:
```bash
npm run build --prod
```
Os arquivos de build serão gerados na pasta dist/.

## Docker

Para construir e rodar o frontend com Docker:

1. **Construir a Imagem Docker**
    ```bash
        docker build -t meu-frontend-angular .
 
    ```
2. **Rodar o Contêiner**    
    ```bash
    docker run -p 80:80 meu-frontend-angular
    ```
Acesse o aplicativo em http://localhost:80.

