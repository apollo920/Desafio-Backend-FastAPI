from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.opcao_resposta import OpcaoResposta
from app.schemas.opcao_resposta import OpcaoRespostaCreate, OpcaoRespostaOut

router = APIRouter(prefix="/opcoes-resposta", tags=["Opções de Resposta"])

@router.post("/", response_model=OpcaoRespostaOut)
def criar_opcao(opcao: OpcaoRespostaCreate, db: Session = Depends(get_db)):
    nova = OpcaoResposta(**opcao.dict())
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova

# @router.get("/pergunta/{pergunta_id}", response_model=list[OpcaoRespostaOut])
# def listar_opcoes(pergunta_id: int, db: Session = Depends(get_db)):
#     return db.query(OpcaoResposta).filter(OpcaoResposta.pergunta_id == pergunta_id).order_by(OpcaoResposta.ordem).all()

@router.get("/{id}", response_model=OpcaoRespostaOut)
def get_opcao(id: int, db: Session = Depends(get_db)):
    opcao = db.query(OpcaoResposta).get(id)
    if not opcao:
        raise HTTPException(status_code=404, detail="Opção não encontrada")
    return opcao

@router.put("/{id}", response_model=OpcaoRespostaOut)
def atualizar_opcao(id: int, dados: OpcaoRespostaCreate, db: Session = Depends(get_db)):
    opcao = db.query(OpcaoResposta).get(id)
    if not opcao:
        raise HTTPException(status_code=404, detail="Opção não encontrada")
    
    for campo, valor in dados.dict().items():
        setattr(opcao, campo, valor)
    
    db.commit()
    db.refresh(opcao)
    return opcao

@router.delete("/{id}")
def deletar_opcao(id: int, db: Session = Depends(get_db)):
    opcao = db.query(OpcaoResposta).get(id)
    if not opcao:
        raise HTTPException(status_code=404, detail="Opção não encontrada")
    db.delete(opcao)
    db.commit()
    return {"ok": True}
