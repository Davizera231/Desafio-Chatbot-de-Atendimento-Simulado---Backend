# Desafio-Chatbot-de-Atendimento-Simulado---Backend 

# Sobre o Projeto 
Este projeto consiste em um sistema backend para um chatbot de atendimento simulado desenvolvido em Django e Django REST Framework. A aplicação oferece uma API RESTful para gerenciar conversas entre usuários e um chatbot, permitindo o envio de mensagens e a recuperação do histórico de conversas específico para cada usuário.

O sistema simula um ambiente de atendimento onde diferentes usuários (A e B) recebem respostas personalizadas do chatbot, com todas as interações sendo armazenadas em banco de dados para consulta posterior. 

#
# Tecnologias Utilizadas 

## Backend 
* Python 3.x
* Django 5.2.8
* Django REST Framework 
* SQLite 
#
## Segurança e Configuração 
* Django CORS Headers
* REST Framework Permissions

#
## Pré-requisitos
* Python 3.8+
* Django 5.2.8
* Django REST Framework
* Django CORS Headers

#
# Instalação das dependências
```
pip install django djangorestframework django-cors-headers

```
#
# Instalação do projeto
## 1. Clone o repositório
```
git clone https://github.com/seu-usuario/chatbot-backend.git

``` 
#
## 2. Navegue até o diretório do projeto
```
cd Chatbot_de_atendimento_simulado_backend

``` 
#
## 3. Execute o servidor de desenvolvimento
```
python manage.py runserver

``` 

# Estrutura do Banco de dados
## Modelo: Message
```
Campo	            Tipo	                    Descrição

id	            BigAutoField	        Chave primária automática
user	            CharField	        Identificador do usuário (A ou B)
question	    TextField	            Mensagem enviada pelo usuário
response	    TextField	            Resposta do chatbot
created_at	    DateTimeField	        Data e hora de criação (automático)

```
#
# Endpoints da API 
## Base URL 
```
http://localhost:8000/api/chat/

```
#
## Endpoints Disponíveis
## Endpoint: Enviar Mensagem - POST
Descrição: Envia uma mensagem do usuário para o chatbot e recebe uma resposta personalizada.
#
## URL:
```
POST /api/chat/send/

```
#
## Body:
```
{
    "user":"A",
    "message":"Olá, preciso de ajuda"
}

```
### Respostas: 
### 200 OK - Mensagem processada com sucesso 
```
{
    "user": "A",
    "question": "Olá, preciso de ajuda",
    "response": "Usuário A, obrigado pelo contato!"
}

```
### 400 Bad Request - Dados inválidos
```
{
    "error": "Campos 'user' e 'message' são obrigatórios"
}

``` 
#
# Endpoint: Obter Histórico - GET 
Descrição: Recupera o histórico completo de mensagens de um usuário especifico.
### URL: 
```
GET /api/chat/history/{user_id}/

```
### Parâmetros: 
* user_id: Identificador do usuário (A ou B)
### Exemplo: 
```
GET /api/chat/history/A/

```
### Respostas: 
### 200 OK - Histórico recuperado com sucesso
```
[
    {
        "id": 1,
        "user": "A",
        "question": "Olá, preciso de ajuda",
        "response": "Usuário A, obrigado pelo contato!",
        "created_at": "2024-01-15T10:30:00Z"
    },
    {
        "id": 2,
        "user": "A",
        "question": "Como posso resetar minha senha?",
        "response": "Usuário A, obrigado pelo contato!",
        "created_at": "2024-01-15T10:32:00Z"
    }
]

``` 
### 200 OK - Nenhuma mensagem encontrada 
```
[]

``` 

### 400 Bad Request - ID de usuário inválido 
```
{
    "error": "ID de usuário deve ser 'A' ou 'B'"
}

```
#
# Estrutura do projeto
```
Chatbot_de_atendimento_simulado_backend/
├── chat/                          
│   ├── migrations/               
│   ├── __init__.py
│   ├── admin.py                  
│   ├── apps.py                   
│   ├── models.py                 
│   ├── serializers.py            
│   ├── urls.py                   
│   └── views.py                  
├── settings.py                   
├── urls.py                       
├── wsgi.py                       
├── asgi.py                       
└── manage.py                     

```
# Funcionalidade do Chatbot

## Resposta Personalizadas por usuário 
* Usuário A: Recebe a resposta: "Usuário A, obrigado pelo contato!"
* Usuário B: Recebe a resposta: "Usuário B, sua mensagem foi recebida!"

# Persistência de dados
* Identificação do usuário
* Mensagem enviada
* Resposta do chatbot
* Timestamp da interação



