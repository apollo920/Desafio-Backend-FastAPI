from pydantic import BaseModel
from typing import Optional

class OpcaoRespostaBase(BaseModel):
    resposta: str
    ordem: Optional[int] = 0
    resposta_aberta: Optional[bool] = False

class OpcaoRespostaCreate(OpcaoRespostaBase):
    pass

class OpcaoRespostaOut(OpcaoRespostaBase):
    id: int

    class Config:
        orm_mode = True
