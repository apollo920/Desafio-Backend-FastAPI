from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Pergunta(Base):
    __tablename__ = "perguntas"

    id = Column(Integer, primary_key=True, index=True)
    formulario_id = Column(Integer, ForeignKey("formularios.id"), nullable=False)
    enunciado = Column(String, nullable=False)
    tipo = Column(String, nullable=False)  # exemplo: texto, numero, data
    obrigatoria = Column(Boolean, default=False)
    ordem = Column(Integer, nullable=False)

    # Relacionamento (opcional)
    formulario = relationship("Formulario", backref="perguntas")
