from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional, List

from app.database import SessionLocal
from app.schemas import pergunta as schemas
from app.models import pergunta as models
from app.models.formulario import Formulario
from app.models.opcao_resposta import OpcaoResposta
from app.models.formulario import Formulario
from app.models.formulario import Formulario


router = APIRouter(
    prefix="/pergunta",
    tags=["Pergunta"],
    responses={404: {"description": "Not found"}},
)


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


@router.get("/{formulario_id}/perguntas", response_model=List[schemas.PerguntaOut])
def listar_perguntas(
    formulario_id: int,
    db: Session = Depends(get_db),
    tipo: Optional[str] = Query(None, description="Filtrar por tipo da pergunta"),
    obrigatoria: Optional[bool] = Query(None, description="Filtrar por obrigatoriedade"),
    order_by: Optional[str] = Query("ordem", description="Campo para ordenar (ex: ordem, tipo)"),
    sort_order: Optional[str] = Query("asc", description="asc ou desc"),
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0)
):
    # Verificar se o formulário existe
    formulario = db.query(Formulario).filter(Formulario.id == formulario_id).first()
    if not formulario:
        raise HTTPException(status_code=404, detail="Formulário não encontrado")

    # Base query
    query = db.query(models.Pergunta).filter(models.Pergunta.formulario_id == formulario_id)

    # Filtros
    if tipo:
        query = query.filter(models.Pergunta.tipo == tipo)
    if obrigatoria is not None:
        query = query.filter(models.Pergunta.obrigatoria == obrigatoria)

    # Ordenação
    if hasattr(models.Pergunta, order_by):
        coluna = getattr(models.Pergunta, order_by)
        if sort_order.lower() == "desc":
            coluna = coluna.desc()
        else:
            coluna = coluna.asc()
        query = query.order_by(coluna)

    # Paginação
    perguntas = query.offset(offset).limit(limit).all()
    return perguntas


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
