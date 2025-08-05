from fastapi import FastAPI
from app.database import Base, engine
from app.routers import formulario, pergunta

app = FastAPI(title="Formulários Dinâmicos API")

app.include_router(formulario.router, prefix="/formularios", tags=["Formulários"])
app.include_router(pergunta.router, prefix="/perguntas", tags=["Perguntas"])

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"mensagem: " "API de Formulários Dinâmicos rodando com sucesso!"}