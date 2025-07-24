from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.services.obterArquivos import iniciar_arquivos
from app.api.endpoints import estados, cidades





@asynccontextmanager
async def lifespan(app: FastAPI):
    # Código de inicialização (startup)
    iniciar_arquivos()

    
    yield


    # Código de finalização (shutdown)

    
    
    
    
app = FastAPI(lifespan= lifespan)


# Inclui os roteadores
app.include_router(estados.router)
app.include_router(cidades.router)
