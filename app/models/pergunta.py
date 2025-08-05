from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Pergunta(Base):
    __tablename__ = "pergunta"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String)
    codigo = Column(String)
    orientacao_resposta = Column(String)
    ordem = Column(Integer)
    obrigatoria = Column(Boolean)
    sub_pergunta = Column(Boolean)
    tipo = Column(String, index=True)

    formulario_id = Column(Integer, ForeignKey("formularios.id"), nullable=False)
    formulario = relationship("Formulario", back_populates="perguntas")

    opcoes = relationship("OpcaoResposta", back_populates="pergunta", cascade="all, delete-orphan")
    opcoes_relacionadas = relationship("OpcaoRespostaPergunta", back_populates="pergunta", cascade="all, delete-orphan")
