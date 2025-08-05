from datetime import datetime
from pydantic import BaseModel

class FormularioBase(BaseModel):
    titulo: str
    descricao: str | None = None

class FormularioCreate(FormularioBase):
    pass

class FormularioOut(FormularioBase):
    id: int

    class Config:
        orm_mode = True
