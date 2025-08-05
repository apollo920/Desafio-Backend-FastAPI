from datetime import datetime
from pydantic import BaseModel

class FormularioBase(BaseModel):
    titulo: str
    descricao: str | None = None

class FormularioCreate(FormularioBase):
    pass

class FormularioOut(FormularioBase):
    id: int
    criado_em: datetime

    class Config:
        orm_mode = True
