from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.services.obterDataBase import iniciar_arquivos
from app.api.endpoints import *

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Código de inicialização (startup)
    iniciar_arquivos()
    yield
    # Código de encerramento (shutdown), se quiser
    # ex: limpar arquivos temporários
    # limpar_arquivos_temporarios()
    
app = FastAPI(
    lifespan=lifespan,
    title="API de Dados Climáticos do Brasil",
    description="""
Esta API fornece **dados climáticos históricos** do Brasil.

## Principais Rotas

- ✅ **Pesquisa Simples**  
  Gera um gráfico com parâmetros definidos internamente para variáveis climáticas e modos de agrupamento.
  
- ✅ **Pesquisa "Dia Mais"**  
  Gera um gráfico do *dia mais* (ex.: dia mais quente, dia mais frio, dia mais chuvoso) de um período de tempo.  
  Se o período não for informado, a busca será feita em todos os anos disponíveis.

- ✅ **Pesquisa Avançada**  
  Gera um gráfico de até **5 variáveis climáticas**, permitindo configurar o processamento interno (mais informaçoes abaixo): 

Para mais informacoes acesse `/dock_interna`."

---

**Contato:**  
📧 Email: [thiagoweiss007@gmail.com](mailto:thiagoweiss007@gmail.com)  
💻 GitHub: [Thiago-Weiss](https://github.com/Thiago-Weiss/Projeto-api-cidades)
""",
    version="1.0.0",
    contact={
        "name": "Thiago Weiss Silva",
        "email": "thiagoweiss007@gmail.com",
    }
)
    


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
app.include_router(dockInterna.router)
app.include_router(pesquisaSimples.router)
app.include_router(pesquisaAvancada.router)
app.include_router(pesquisaDiaMais.router)

app.include_router(estados.router)
app.include_router(cidades.router)

# remover futuramente
app.include_router(grafico.router)
app.include_router(acordar.router)

