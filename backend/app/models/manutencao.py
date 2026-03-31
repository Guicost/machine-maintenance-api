from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class Manutencao(Base):
    __tablename__ = "manutencoes"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String, nullable=False)
    tipo = Column(String, nullable=False)
    status = Column(String, nullable=False)

    maquina_id = Column(Integer, ForeignKey("maquinas.id"))