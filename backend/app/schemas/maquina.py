from pydantic import BaseModel
from typing import List
from app.schemas.manutencao import ManutencaoSimples

class MaquinaBase(BaseModel):
    nome: str
    modelo: str
    status: str

class MaquinaCreate(MaquinaBase):
    pass

class MaquinaUpdate(MaquinaBase):
    pass

class MaquinaResponse(MaquinaBase):
    id: int

    class Config:
        from_attributes = True

class MaquinaComManutencoes(MaquinaBase):
    id: int
    manutencoes: List[ManutencaoSimples] = []

    class Config:
        from_attributes = True