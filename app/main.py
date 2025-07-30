from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.services.obterDataBase import iniciar_arquivos
from app.api.endpoints import estados, cidades, grafico, pesquisaClima

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Código de inicialização (startup)
    iniciar_arquivos()
    yield
    # Código de encerramento (shutdown), se quiser
    # ex: limpar arquivos temporários
    # limpar_arquivos_temporarios()
    
app = FastAPI(lifespan=lifespan)


# Adicionando o middleware CORS corretamente
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens, cuidado com segurança em produção
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos HTTP (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos os cabeçalhos
)




@app.get("/", include_in_schema= False)
async def go_docs():
    return RedirectResponse(url= "/docs")

# Inclui os roteadores
app.include_router(estados.router)
app.include_router(cidades.router)
app.include_router(grafico.router)
app.include_router(pesquisaClima.router)

