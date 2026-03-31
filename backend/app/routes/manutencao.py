from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.manutencao import Manutencao
from app.models.maquina import Maquina
from app.schemas.manutencao import ManutencaoCreate
from app.deps import get_db

router = APIRouter(prefix="/manutencoes", tags=["Manutenções"])

@router.post("/")
def criar_manutencao(manutencao: ManutencaoCreate, db: Session = Depends(get_db)):
    maq = db.query(Maquina).filter(Maquina.id == manutencao.maquina_id).first()

    if not maq:
        raise HTTPException(status_code=404, detail="Máquina não encontrada")

    nova = Manutencao(**manutencao.dict())
    db.add(nova)
    db.commit()
    db.refresh(nova)

    return nova

@router.get("/")
def listar_manutencoes(db: Session = Depends(get_db)):
    return db.query(Manutencao).all()

@router.delete("/{id}")
def deletar_manutencao(id: int, db: Session = Depends(get_db)):
    manut = db.query(Manutencao).filter(Manutencao.id == id).first()

    if not manut:
        raise HTTPException(status_code=404, detail="Manutenção não encontrada")

    db.delete(manut)
    db.commit()

    return {"mensagem": "Manutenção removida"}