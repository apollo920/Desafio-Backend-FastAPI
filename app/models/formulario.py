from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Formulario(Base):
    __tablename__ = "formularios"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    descricao = Column(String)
    ordem = Column(Integer)

    perguntas = relationship("Pergunta", back_populates="formulario", cascade="all, delete-orphan")
