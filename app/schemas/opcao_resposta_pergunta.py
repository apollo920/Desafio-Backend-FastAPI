from pydantic import BaseModel
from typing import Optional

class OpcaoRespostaPerguntaCreate(BaseModel):
    opcao_resposta_id: int
    pergunta_id: int

class OpcaoRespostaPerguntaOut(BaseModel):
    id: int
    opcao_resposta_id: int
    pergunta_id: int

    class Config:
        from_attributes = True 
