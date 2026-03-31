from pydantic import BaseModel

class ManutencaoBase(BaseModel):
    descricao: str
    tipo: str
    status: str
    maquina_id: int

class ManutencaoCreate(ManutencaoBase):
    pass

class ManutencaoSimples(BaseModel):
    id: int
    descricao: str
    tipo: str
    status: str

    class Config:
        from_attributes = True

class ManutencaoResponse(ManutencaoBase):
    id: int

    class Config:
        from_attributes = True