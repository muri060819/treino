# 📘 Atividade: Construindo APIs REST com FastAPI

## 🎯 Objetivo

Aprenda a criar uma API REST com FastAPI, expondo endpoints para consultar e modificar recursos. Ao final, você terá uma API simples de livros com validação de dados e respostas HTTP adequadas.

## 📝 Tarefas

### 🛠️ Criar a Aplicação e um Endpoint

#### Descrição
Use o arquivo inicial fornecido para executar uma aplicação FastAPI e criar um endpoint simples de verificação. Explore também a documentação interativa gerada pelo framework.

#### Requisitos
O programa concluído deve:

- Criar uma aplicação FastAPI no arquivo `starter-code.py`.
- Implementar `GET /health` para retornar `{"status": "ok"}`.
- Iniciar a aplicação e confirmar que `GET /docs` exibe a documentação interativa.

Para instalar as dependências e executar o arquivo:

```bash
python -m pip install fastapi uvicorn
python assignments/fastapi-rest-api/starter-code.py
```


### 🛠️ Criar Endpoints para Listar e Cadastrar Livros

#### Descrição
Amplie a API para gerenciar livros em memória. Cada livro deve ter um identificador, título e autor; use um modelo Pydantic para validar os dados enviados ao cadastrar um livro.

#### Requisitos
O programa concluído deve:

- Implementar `GET /books` para retornar a lista de livros.
- Implementar `POST /books` para cadastrar um livro com título e autor.
- Gerar um identificador para cada livro e responder com status HTTP `201 Created` ao cadastrá-lo.
- Rejeitar dados de entrada inválidos usando a validação do FastAPI/Pydantic.


### 🛠️ Consultar, Atualizar e Remover um Livro

#### Descrição
Complete a API implementando operações para acessar um livro específico. Use os identificadores para localizar o recurso e informe claramente quando ele não existir.

#### Requisitos
O programa concluído deve:

- Implementar `GET /books/{book_id}` para retornar um livro pelo identificador.
- Implementar `PUT /books/{book_id}` para atualizar o título e o autor de um livro existente.
- Implementar `DELETE /books/{book_id}` para remover um livro existente.
- Retornar status HTTP `404 Not Found` quando o identificador não corresponder a um livro.
- Testar os endpoints pela documentação interativa em `/docs`.
