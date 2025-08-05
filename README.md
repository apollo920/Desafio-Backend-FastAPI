# 📘 API de Formulários Dinâmicos – FastAPI + PostgreSQL

Este projeto é uma API RESTful desenvolvida com **FastAPI** e **SQLAlchemy** para manipular formulários dinâmicos com perguntas e opções de resposta. Utiliza **PostgreSQL** como banco de dados e suporta funcionalidades como criação de formulários, perguntas, filtros e paginação.

---

## 📦 Tecnologias Utilizadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [Uvicorn](https://www.uvicorn.org/)
- [Pydantic](https://docs.pydantic.dev/)
- [Python 3.11+](https://www.python.org/)

---

## 🚀 Pré-requisitos

- Python 3.11+ instalado
- PostgreSQL instalado e configurado

---

## 🛠️ Passo a passo de instalação

### 1. 📥 Clone o repositório

```bash
git clone https://github.com/apollo920/Desafio-Backend-FastAPI.git
cd Desafio-Backend-FastAPI
```

---

### 2. 🐘 Instale o PostgreSQL

Caso ainda não tenha, instale:

- No Ubuntu:
  ```bash
  sudo apt update
  sudo apt install postgresql postgresql-contrib
  ```

- No Windows, baixe aqui: https://www.postgresql.org/download/windows/

---

### 3. 🐍 Crie o ambiente virtual

```bash
python -m venv .venv
```

Ative o ambiente:

- No **Windows**:
  ```bash
  .venv\Scripts\activate
  ```

- No **Linux/macOS**:
  ```bash
  source .venv/bin/activate
  ```

---

### 4. 📦 Instale as dependências

```bash
pip install -r requirements.txt
```

---

### 5. ⚙️ Configure o arquivo `.env`

Crie um arquivo `.env` na raiz com base no `.env.example`:

```bash
cp .env.example .env
```

Edite o `.env` com sua configuração local. Exemplo:

```env
DATABASE_URL=postgresql://usuario:senha@localhost:5432/fastapi
SERVER_PORT=8000
DEBUG=true
```

> 🔐 **Importante:** Substitua `"senha"` pela senha real do seu PostgreSQL.

---

### 6. 🏗️ Inicialize o banco

No primeiro run da aplicação, as tabelas serão criadas automaticamente com `Base.metadata.create_all()`.

---

### 7. ▶️ Rode o servidor FastAPI

Execute:

```bash
uvicorn app.main:app --reload
```

---

## 🌐 Como acessar a API

Após rodar o servidor, acesse:

### 🧪 Documentação Interativa (Swagger UI)

> [http://localhost:8000/docs](http://localhost:8000/docs)

### 📜 Documentação alternativa (ReDoc)

> [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🧪 Testando rapidamente

Crie um formulário:

```
POST /formularios/
{
  "titulo": "Formulário de exemplo",
  "descricao": "Formulário teste",
  "ordem": 1
}
```

Liste perguntas de um formulário:

```
GET /perguntas/formulario/1
```

---

## 📂 Estrutura de Pastas

```
app/
├── main.py
├── core/
│   └── config.py
├── database.py
├── models/
│   ├── formulario.py
│   ├── pergunta.py
│   └── opcao_resposta.py
├── routers/
│   ├── formulario.py
│   ├── pergunta.py
│   └── opcao_resposta.py
├── schemas/
│   ├── formulario.py
│   ├── pergunta.py
│   └── opcao_resposta.py
```

---