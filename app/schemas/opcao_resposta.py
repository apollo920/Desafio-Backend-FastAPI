from pydantic import BaseModel
from typing import Optional

class OpcaoRespostaBase(BaseModel):
    resposta: str
    ordem: Optional[int] = None
    resposta_aberta: Optional[bool] = False

class OpcaoRespostaCreate(OpcaoRespostaBase):
    id_pergunta: int

class OpcaoRespostaUpdate(OpcaoRespostaBase):
    pass

class OpcaoRespostaOut(BaseModel):
    id: int
    descricao: str
    ordem: int

    class Config:
        orm_mode = True
