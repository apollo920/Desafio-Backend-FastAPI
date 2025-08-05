from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas import pergunta as schemas
from app.models import pergunta as models

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.PerguntaOut)
def criar_pergunta(pergunta: schemas.PerguntaCreate, db: Session = Depends(get_db)):
    nova = models.Pergunta(**pergunta.dict())
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova


@router.get("/formulario/{formulario_id}", response_model=list[schemas.PerguntaOut])
def listar_perguntas(
    formulario_id: int,
    tipo: str = Query(None),
    obrigatoria: bool = Query(None),
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
):
    query = db.query(models.Pergunta).filter(models.Pergunta.formulario_id == formulario_id)

    if tipo:
        query = query.filter(models.Pergunta.tipo == tipo)
    if obrigatoria is not None:
        query = query.filter(models.Pergunta.obrigatoria == obrigatoria)

    return query.order_by(models.Pergunta.ordem.asc()).offset(skip).limit(limit).all()


@router.put("/{pergunta_id}", response_model=schemas.PerguntaOut)
def atualizar_pergunta(pergunta_id: int, dados: schemas.PerguntaCreate, db: Session = Depends(get_db)):
    pergunta = db.query(models.Pergunta).get(pergunta_id)
    if not pergunta:
        raise HTTPException(status_code=404, detail="Pergunta não encontrada")
    for campo, valor in dados.dict().items():
        setattr(pergunta, campo, valor)
    db.commit()
    db.refresh(pergunta)
    return pergunta


@router.delete("/{pergunta_id}")
def deletar_pergunta(pergunta_id: int, db: Session = Depends(get_db)):
    pergunta = db.query(models.Pergunta).get(pergunta_id)
    if not pergunta:
        raise HTTPException(status_code=404, detail="Pergunta não encontrada")
    db.delete(pergunta)
    db.commit()
    return {"mensagem": "Pergunta deletada com sucesso"}
