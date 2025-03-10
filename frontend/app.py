import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

API_URL = "http://127.0.0.1:8000/preco"
HISTORICO_URL = "http://127.0.0.1:8000/historico"

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

# Obter histórico de preços
if st.button("Mostrar Histórico de Preços"):
    hist_response = requests.get(HISTORICO_URL, params={"cripto": cripto, "dias": 7, "moeda": moeda})
    
    if hist_response.status_code == 200:
        data = hist_response.json()["precos"]
        df = pd.DataFrame(data, columns=["timestamp", "preco"])
        df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")

        # Criar gráfico
        st.subheader(f"📊 Histórico de preços de {cripto} nos últimos 7 dias")
        fig, ax = plt.subplots()
        ax.plot(df["timestamp"], df["preco"], marker="o", linestyle="-")
        ax.set_xlabel("Data")
        ax.set_ylabel(f"Preço em {moeda.upper()}")
        ax.grid()

        st.pyplot(fig)
    else:
        st.error("❌ Erro ao obter histórico de preços.")