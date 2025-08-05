from pydantic import BaseModel
from typing import List, Optional
from app.schemas.opcao_resposta import OpcaoRespostaOut
from app.schemas.opcao_resposta_pergunta import OpcaoRespostaPerguntaCreate

class PerguntaBase(BaseModel):
    formulario_id: int
    titulo: str
    codigo: str
    orientacao_resposta: Optional[str]
    tipo: str
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

class PerguntaComOpcoes(BaseModel):
    id: int
    titulo: str
    codigo: Optional[str]
    orientacao_resposta: Optional[str]
    obrigatoria: Optional[bool]
    sub_pergunta: Optional[bool]
    tipo: Optional[str]
    formulario_id: int
    opcoes_relacionadas: List[OpcaoRespostaPerguntaCreate] = []

    class Config:
        orm_mode = True
