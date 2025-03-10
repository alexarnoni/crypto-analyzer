import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/preco"

st.title("📈 Preço das Criptomoedas")

# Lista de criptomoedas populares
criptomoedas = [
    "bitcoin", "ethereum", "dogecoin", "ripple", "litecoin", "cardano",
    "polkadot", "solana", "binancecoin", "shiba-inu"
]

# Criando dropdown para escolher a criptomoeda
cripto = st.selectbox("Escolha uma criptomoeda:", criptomoedas)

# Campo para escolher a moeda
moeda = st.text_input("Digite a moeda:", "usd")

# Botão para obter preço
if st.button("Obter Preço"):
    response = requests.get(API_URL, params={"cripto": cripto, "moeda": moeda})
    
    if response.status_code == 200:
        preco = response.json()
        if cripto in preco and moeda in preco[cripto]:
            st.success(f"💰 O preço atual de {cripto} em {moeda.upper()} é: {preco[cripto][moeda]}")
        else:
            st.warning("⚠️ Dados não disponíveis para essa criptomoeda e moeda.")
    else:
        st.error("❌ Erro ao obter preço. Tente novamente mais tarde.")
