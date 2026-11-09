# 📘 Atividade: Testando APIs com pytest

## 🎯 Objetivo

Aprenda a verificar o comportamento de uma API REST com pytest e o cliente de testes do FastAPI, sem iniciar um servidor. Você escreverá testes para respostas, operações de livros e casos de erro.

## 📝 Tarefas

### 🛠️ Testar Endpoints Básicos

#### Descrição
Use a API fornecida em `starter-code.py` e crie `test_api.py`. Comece testando o endpoint de saúde e a listagem de livros com o `TestClient`.

#### Requisitos
O programa concluído deve:

- Criar um `TestClient` para a aplicação FastAPI fornecida.
- Verificar que `GET /health` retorna status `200` e o JSON `{"status": "ok"}`.
- Verificar que `GET /books` retorna status `200` e uma lista JSON.
- Executar os testes com `pytest`.

Instale as dependências e execute os testes a partir da raiz do projeto:

```bash
python -m pip install fastapi pytest httpx2
pytest assignments/testing-fastapi-api/test_api.py
```


### 🛠️ Testar Criação e Validação de Livros

#### Descrição
Escreva testes para cadastrar livros e confirmar que a API aceita dados válidos e rejeita dados incompletos. Confira tanto o status HTTP quanto o conteúdo das respostas.

#### Requisitos
O programa concluído deve:

- Verificar que `POST /books` com título e autor retorna status `201`.
- Confirmar que a resposta inclui um identificador, o título e o autor enviados.
- Verificar que um corpo sem os campos obrigatórios retorna status `422`.
- Usar asserções que expliquem quais resultados são esperados.


### 🛠️ Testar Operações e Casos de Erro

#### Descrição
Teste a consulta, atualização e remoção de livros. Garanta também que as respostas indiquem corretamente quando o recurso solicitado não existe.

#### Requisitos
O programa concluído deve:

- Testar `GET /books/{book_id}`, `PUT /books/{book_id}` e `DELETE /books/{book_id}` para um livro existente.
- Verificar que as operações de atualização e remoção retornam os status e dados esperados.
- Verificar que a consulta, atualização ou remoção de um identificador inexistente retorna status `404`.
- Manter cada teste independente, preparando ou limpando os dados necessários para que a ordem de execução não altere os resultados.
