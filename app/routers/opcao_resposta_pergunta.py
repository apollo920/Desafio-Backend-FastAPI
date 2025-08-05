from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.opcao_resposta_pergunta import OpcaoRespostaPergunta
from app.schemas.opcao_resposta_pergunta import OpcaoRespostaPerguntaCreate, OpcaoRespostaPerguntaOut

router = APIRouter(prefix="/opcao_resposta", tags=["Opções por Pergunta"])

@router.post("/", response_model=OpcaoRespostaPerguntaOut)
def associar_opcao_a_pergunta(data: OpcaoRespostaPerguntaCreate, db: Session = Depends(get_db)):
    nova = OpcaoRespostaPergunta(**data.dict())
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova

@router.get("/pergunta/{pergunta_id}", response_model=list[OpcaoRespostaPerguntaOut])
def listar_opcoes_por_pergunta(pergunta_id: int, db: Session = Depends(get_db)):
    return db.query(OpcaoRespostaPergunta).filter(OpcaoRespostaPergunta.pergunta_id == pergunta_id).all()

@router.put("/{id}", response_model=OpcaoRespostaPerguntaOut)
def atualizar_associacao(id: int, dados: OpcaoRespostaPerguntaCreate, db: Session = Depends(get_db)):
    item = db.query(OpcaoRespostaPergunta).get(id)
    if not item:
        raise HTTPException(status_code=404, detail="Associação não encontrada")
    
    for campo, valor in dados.dict().items():
        setattr(item, campo, valor)

    db.commit()
    db.refresh(item)
    return item

@router.delete("/{id}")
def remover_associacao(id: int, db: Session = Depends(get_db)):
    item = db.query(OpcaoRespostaPergunta).get(id)
    if not item:
        raise HTTPException(status_code=404, detail="Associação não encontrada")
    db.delete(item)
    db.commit()
    return {"ok": True}
