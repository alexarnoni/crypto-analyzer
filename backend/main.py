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

@app.get("/historico")
def obter_historico(cripto: str = "bitcoin", dias: int = 7, moeda: str = "usd"):
    """Obtém o histórico de preços da criptomoeda"""
    response = requests.get(f"{COINGECKO_URL}/coins/{cripto}/market_chart",
                            params={"vs_currency": moeda, "days": dias})
    
    if response.status_code == 200:
        data = response.json()
        return {"precos": data["prices"]}
    
    return {"erro": "Não foi possível obter o histórico"}