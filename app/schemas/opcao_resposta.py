from pydantic import BaseModel
from typing import Optional

class OpcaoRespostaBase(BaseModel):
    resposta: str
    ordem: Optional[int] = 0
    resposta_aberta: Optional[bool] = False

class OpcaoRespostaCreate(OpcaoRespostaBase):
    id_pergunta: int

class OpcaoRespostaOut(OpcaoRespostaBase):
    id: int
    id_pergunta: int

    class Config:
        orm_mode = True
