from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class OpcaoResposta(Base):
    __tablename__ = "opcao_resposta"

    id = Column(Integer, primary_key=True, index=True)
    pergunta_id = Column(Integer, ForeignKey("pergunta.id"))
    resposta = Column(String, nullable=False)
    ordem = Column(Integer)
    resposta_aberta = Column(Boolean, default=False)

    pergunta = relationship("Pergunta", back_populates="opcoes")
    opcoes_pergunta = relationship("OpcaoRespostaPergunta", back_populates="opcao_resposta", cascade="all, delete-orphan")
