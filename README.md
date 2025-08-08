# 📍 Brasil ClimaAPI

**Brasil ClimaAPI** é uma API desenvolvida em **Python** utilizando **FastAPI** e **Pandas**, que fornece dados climaticos historicos do Brasil, para o front end [aqui](link para o front), ou se quiser acessar diretamente a api [aqui](https://projeto-clima-web-back.onrender.com/docs) *(pode levar alguns segundos para o servidor iniciar)*, com essa api é possivel obter os dados reais e preciso para gerar graficos


---

## Princiapis rotas /Funcionalidades

- ✅ **Pesquisa Simples**  
  Gera um gráfico com parâmetros definidos internamente para variáveis climáticas e modos de agrupamento (link do readme).
  
- ✅ **Pesquisa "Dia Mais"**  
  Gera um gráfico do *dia mais* (ex.: dia mais quente, dia mais frio, dia mais chuvoso) de um período de tempo.  
  Se o período não for informado, a busca será feita em todos os anos disponíveis.

- ✅ **Pesquisa Avançada**  
  Gera um gráfico de até **5 variáveis climáticas** (link do readme), permitindo configurar o processamento interno (link do readme): 


---

## 🛠️ Principais Tecnologias utilizadas

- [Python] Linguagem de programaçao
- [FastAPI] Fazer o Back End
- [Pandas] Trabalhar com os dados
- [Uvicorn] para rodar o servidor

---

## 📂 Estrutura do projeto
app/  
├── main.py # Inicializa a API FastAPI  
├── api/ # Rotas da API  
├── core/ # Constantes, schemas e configs  
├── data/ # Dados em Parquet  
├── services/ # Serviços de gerar os "graficos" e funções auxiliares  
└── requirements.txt # Dependências do projeto  


## 📊 Rotas
![](img/docs.png)

### GET /grafico/pesquisa-simples
![](img/pesquisa_simples.png) ![](img/pesquisa_simples_resposta.png)

### GET /grafico/pesquisa-dia-mais
![](img/pesquisa_dia_mais.png) ![](img/pesquisa_dia_mais_resposta.png)


---

## ▶️ Como rodar o projeto localmente

Clone o repositório
```bash
https://github.com/Thiago-Weiss/Projeto-Clima-Web-Back.git
```
Crie o ambiente virtual do Python
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```
Instale as dependencias
```bash
pip install -r requirements.txt
```
Rode o servidor
```bash
uvicorn app.main:app --reload
ou
python -m uvicorn app.main:app --reload
```
Acesse a api
```bash
http://127.0.0.1:8000/docs
```



📜 Licença
Este projeto está sob a licença MIT. Você pode usá-lo, modificá-lo e distribuí-lo livremente.

