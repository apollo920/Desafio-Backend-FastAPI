from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas import formulario as schemas
from app.models import formulario as models

router = APIRouter()

# Dependency para obter uma sessão DB por requisição
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.FormularioOut)
def criar_formulario(formulario: schemas.FormularioCreate, db: Session = Depends(get_db)):
    novo = models.Formulario(**formulario.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo


@router.get("/", response_model=list[schemas.FormularioOut])
def listar_formularios(db: Session = Depends(get_db)):
    return db.query(models.Formulario).all()


@router.get("/{formulario_id}", response_model=schemas.FormularioOut)
def obter_formulario(formulario_id: int, db: Session = Depends(get_db)):
    formulario = db.query(models.Formulario).get(formulario_id)
    if not formulario:
        raise HTTPException(status_code=404, detail="Formulário não encontrado")
    return formulario


@router.put("/{formulario_id}", response_model=schemas.FormularioOut)
def atualizar_formulario(formulario_id: int, dados: schemas.FormularioCreate, db: Session = Depends(get_db)):
    formulario = db.query(models.Formulario).get(formulario_id)
    if not formulario:
        raise HTTPException(status_code=404, detail="Formulário não encontrado")
    for campo, valor in dados.dict().items():
        setattr(formulario, campo, valor)
    db.commit()
    db.refresh(formulario)
    return formulario


@router.delete("/{formulario_id}")
def deletar_formulario(formulario_id: int, db: Session = Depends(get_db)):
    formulario = db.query(models.Formulario).get(formulario_id)
    if not formulario:
        raise HTTPException(status_code=404, detail="Formulário não encontrado")
    db.delete(formulario)
    db.commit()
    return {"mensagem": "Formulário deletado com sucesso"}
