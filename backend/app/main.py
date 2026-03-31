from fastapi import FastAPI
from app.database import Base, engine

from app.routes import maquina
from app.routes import manutencao

from app.models import maquina as maquina_model
from app.models import manutencao as manutencao_model

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sistema de Manutenção")

app.include_router(maquina.router)
app.include_router(manutencao.router)