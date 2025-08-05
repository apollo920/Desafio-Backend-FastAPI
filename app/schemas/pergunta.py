from pydantic import BaseModel

class PerguntaBase(BaseModel):
    formulario_id: int
    enunciado: str
    tipo: str  # exemplo: texto, numero, data
    obrigatoria: bool
    ordem: int

class PerguntaCreate(PerguntaBase):
    pass

class PerguntaOut(PerguntaBase):
    id: int

    class Config:
        orm_mode = True
