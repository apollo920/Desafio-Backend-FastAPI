from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class OpcaoRespostaPergunta(Base):
    __tablename__ = "opcoes_resposta_pergunta"

    id = Column(Integer, primary_key=True, index=True)
    id_opcao_resposta = Column(Integer, ForeignKey("opcoes_respostas.id"))
    id_pergunta = Column(Integer, ForeignKey("pergunta.id"))

    opcao_resposta = relationship("OpcaoResposta")
    pergunta = relationship("Pergunta")
