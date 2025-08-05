from pydantic import BaseModel
from typing import List, Optional
from .opcao_resposta import OpcaoRespostaOut

class PerguntaBase(BaseModel):
    formulario_id: int
    titulo: str
    codigo: str
    orientacao_resposta: Optional[str]
    tipo_pergunta: str
    obrigatoria: bool
    ordem: int
    sub_pergunta: bool
class PerguntaCreate(PerguntaBase):
    pass

class PerguntaOut(BaseModel):
    id: int
    titulo: Optional[str]
    codigo: Optional[str]
    orientacao_resposta: Optional[str]
    ordem: int
    obrigatoria: bool
    sub_pergunta: bool
    tipo: str
    formulario_id: int
    opcoes: List[OpcaoRespostaOut] = []

    class Config:
        orm_mode = True
