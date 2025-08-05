from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from app.database import Base, engine
from app.routers import formulario, pergunta, opcao_resposta


app = FastAPI(title="Formulários Dinâmicos API")

app.include_router(formulario.router, prefix="/formularios", tags=["Formulários"])
app.include_router(pergunta.router, prefix="/perguntas", tags=["Pergunta"])
app.include_router(opcao_resposta.router, prefix="/opcoes-respostas", tags=["Opções de Resposta"])
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"mensagem": "API de Formulários Dinâmicos rodando com sucesso!"}