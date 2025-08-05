from pydantic import BaseModel

class OpcaoRespostaPerguntaBase(BaseModel):
    id_opcao_resposta: int
    id_pergunta: int

class OpcaoRespostaPerguntaCreate(OpcaoRespostaPerguntaBase):
    pass

class OpcaoRespostaPerguntaOut(OpcaoRespostaPerguntaBase):
    id: int

    class Config:
        orm_mode = True
