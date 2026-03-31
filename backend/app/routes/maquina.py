from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models.maquina import Maquina
from app.schemas.maquina import MaquinaCreate, MaquinaUpdate, MaquinaComManutencoes
from app.deps import get_db

router = APIRouter(prefix="/maquinas", tags=["Máquinas"])


@router.post("/", status_code=201)
def criar_maquina(maquina: MaquinaCreate, db: Session = Depends(get_db)):
    nova = Maquina(**maquina.dict())

    db.add(nova)
    db.commit()
    db.refresh(nova)

    return {
        "mensagem": "Máquina cadastrada com sucesso",
        "dados": nova
    }


@router.get("/")
def listar_maquinas(db: Session = Depends(get_db)):
    maquinas = db.query(Maquina).all()

    return {
        "total": len(maquinas),
        "dados": maquinas
    }


@router.get("/{id}")
def buscar_maquina(id: int, db: Session = Depends(get_db)):
    maq = db.query(Maquina).filter(Maquina.id == id).first()

    if not maq:
        raise HTTPException(
            status_code=404,
            detail="Máquina não encontrada ou já removida do sistema"
        )

    return {
        "dados": maq
    }


@router.put("/{id}")
def atualizar_maquina(id: int, maquina: MaquinaUpdate, db: Session = Depends(get_db)):
    maq = db.query(Maquina).filter(Maquina.id == id).first()

    if not maq:
        raise HTTPException(
            status_code=404,
            detail="Não foi possível atualizar: máquina não encontrada"
        )

    maq.nome = maquina.nome
    maq.modelo = maquina.modelo
    maq.status = maquina.status

    db.commit()
    db.refresh(maq)

    return {
        "mensagem": "Máquina atualizada com sucesso",
        "dados": maq
    }


@router.delete("/{id}")
def deletar_maquina(id: int, db: Session = Depends(get_db)):
    maq = db.query(Maquina).filter(Maquina.id == id).first()

    if not maq:
        raise HTTPException(
            status_code=404,
            detail="Não foi possível remover: máquina não encontrada"
        )

    db.delete(maq)
    db.commit()

    return {
        "mensagem": "Máquina removida com sucesso",
        "id_removido": id
    }


@router.get("/{id}/com-manutencoes", response_model=MaquinaComManutencoes)
def buscar_maquina_com_manutencoes(id: int, db: Session = Depends(get_db)):
    maq = db.query(Maquina).filter(Maquina.id == id).first()

    if not maq:
        raise HTTPException(
            status_code=404,
            detail="Máquina não encontrada ou sem registros disponíveis"
        )

    return maq