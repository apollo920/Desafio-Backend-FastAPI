from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class OpcaoRespostaPergunta(Base):
    __tablename__ = "opcao_resposta_pergunta"

    id = Column(Integer, primary_key=True, index=True)
    opcao_resposta_id = Column(Integer, ForeignKey("opcao_resposta.id"))
    pergunta_id = Column(Integer, ForeignKey("pergunta.id"))

    opcao_resposta = relationship("OpcaoResposta", back_populates="opcoes_pergunta")
    pergunta = relationship("Pergunta", back_populates="opcoes_relacionadas")
