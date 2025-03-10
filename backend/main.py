from fastapi import FastAPI
import requests

app = FastAPI()

COINGECKO_URL = "https://api.coingecko.com/api/v3"

@app.get("/")
def home():
    return {"message": "API de Análise de Criptomoedas Rodando!"}

@app.get("/preco")
def obter_preco(cripto: str = "bitcoin", moeda: str = "usd"):
    """Obtém o preço atual da criptomoeda desejada"""
    response = requests.get(f"{COINGECKO_URL}/simple/price",
                            params={"ids": cripto, "vs_currencies": moeda})
    
    if response.status_code == 200:
        return response.json()
    
    return {"erro": "Não foi possível obter o preço"}
