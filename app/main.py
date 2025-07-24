from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.services.obterCidadesEstados.obterArquivo import baixarArquivoCidadesEstados
from app.api.endpoints import estados, cidades





@asynccontextmanager
async def lifespan(app: FastAPI):
    # Código de inicialização (startup)
    baixarArquivoCidadesEstados()
    yield
    # Código de encerramento (shutdown), se quiser
    # ex: limpar arquivos temporários
    # limpar_arquivos_temporarios()
    
app = FastAPI(lifespan= lifespan)


# Inclui os roteadores
app.include_router(estados.router)
app.include_router(cidades.router)
