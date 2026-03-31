from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Maquina(Base):
    __tablename__ = "maquinas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    modelo = Column(String, nullable=False)
    status = Column(String, nullable=False)

    manutencoes = relationship("Manutencao", backref="maquina")