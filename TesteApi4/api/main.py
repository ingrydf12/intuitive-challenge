from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import os

app = FastAPI()

# Configuração do CORS pro frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Tenta carregar o arquivo de relatório
try:
    data = pd.read_csv("api/data/Relatorio_cadop.csv", sep=";", encoding="utf-8")
    if data.empty:
        print("O arquivo CSV está vazio.")
    else:
        print("Arquivo CSV carregado com sucesso.")
except FileNotFoundError:
    print("Arquivo não encontrado. Verifique o caminho.")
    data = pd.DataFrame()
except Exception as e:
    print(f"Erro ao carregar o CSV: {e}")
    data = pd.DataFrame()

# Caso venha vazio
data = data.fillna("")

@app.get("/api/search")
async def search_operadora(q: str = Query(...)):
    resultado = data[
        data["Razao_Social"].str.contains(q, case=False, na=False) | 
        data["Nome_Fantasia"].str.contains(q, case=False, na=False)
    ]
    return resultado.head(10).to_dict(orient="records")

@app.get("/")
def read_root():
    return {"status": "API online"}