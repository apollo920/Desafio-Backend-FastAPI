from sqlalchemy import Column, Integer, String, DateTime, func
from app.database import Base

class Formulario(Base):
    __tablename__ = "formularios"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    descricao = Column(String, nullable=True)
    criado_em = Column(DateTime, server_default=func.now())
