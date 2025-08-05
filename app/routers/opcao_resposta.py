from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.opcao_resposta import OpcaoResposta
from app.schemas.opcao_resposta import OpcaoRespostaCreate, OpcaoRespostaOut

router = APIRouter(prefix="/opcoes-respostas", tags=["Opções de Resposta"])

@router.post("/", response_model=OpcaoRespostaOut)
def criar_opcao(opcao: OpcaoRespostaCreate, db: Session = Depends(get_db)):
    nova = OpcaoResposta(**opcao.dict())
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova

@router.get("/pergunta/{id_pergunta}", response_model=list[OpcaoRespostaOut])
def listar_opcoes(id_pergunta: int, db: Session = Depends(get_db)):
    return db.query(OpcaoResposta).filter(OpcaoResposta.id_pergunta == id_pergunta).order_by(OpcaoResposta.ordem).all()

@router.get("/{id}", response_model=OpcaoRespostaOut)
def get_opcao(id: int, db: Session = Depends(get_db)):
    opcao = db.query(OpcaoResposta).get(id)
    if not opcao:
        raise HTTPException(status_code=404, detail="Opção não encontrada")
    return opcao

@router.delete("/{id}")
def deletar_opcao(id: int, db: Session = Depends(get_db)):
    opcao = db.query(OpcaoResposta).get(id)
    if not opcao:
        raise HTTPException(status_code=404, detail="Opção não encontrada")
    db.delete(opcao)
    db.commit()
    return {"ok": True}
