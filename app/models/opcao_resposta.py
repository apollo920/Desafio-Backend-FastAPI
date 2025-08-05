from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class OpcaoResposta(Base):
    __tablename__ = "opcoes_respostas"

    id = Column(Integer, primary_key=True, index=True)
    id_pergunta = Column(Integer, ForeignKey("pergunta.id"))
    resposta = Column(String)
    ordem = Column(Integer)
    resposta_aberta = Column(Boolean)

    pergunta = relationship("Pergunta", back_populates="opcoes")
