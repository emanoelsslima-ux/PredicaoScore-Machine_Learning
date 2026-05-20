import streamlit as st
import pandas as pd
import joblib

# Configuração da página
st.set_page_config(
    page_title="Predição de Crédito",
    page_icon="📊",
    layout="centered"
)

# Carregar modelo
modelo = joblib.load("modelo.pkl")

# Título
st.title("📊 Predição de Score de Crédito")

st.markdown("""
Preencha os dados abaixo para realizar a previsão utilizando Machine Learning.
""")

st.divider()

# Inputs do usuário

idade = st.slider(
    "Idade",
    18,
    100,
    30
)

salario_anual = st.number_input(
    "Salário Anual",
    min_value=0.0,
    value=50000.0,
    step=1000.0
)

dias_atraso = st.slider(
    "Dias de atraso",
    0,
    100,
    5
)

divida_total = st.number_input(
    "Dívida Total",
    min_value=0.0,
    value=2000.0,
    step=500.0
)

num_cartoes = st.slider(
    "Número de cartões",
    1,
    20,
    3
)

st.divider()

# Botão
if st.button("Realizar previsão"):

    # Criar dataframe
    dados = pd.DataFrame({
        "idade": [idade],
        "salario_anual": [salario_anual],
        "dias_atraso": [dias_atraso],
        "divida_total": [divida_total],
        "num_cartoes": [num_cartoes]
    })

    # Fazer previsão
    previsao = modelo.predict(dados)

    resultado = previsao[0]

    # Resultado
    st.subheader("Resultado")

    if resultado == "Good":
        st.success("🟢 Score GOOD — Cliente aprovado")

    elif resultado == "Standard":
        st.warning("🟡 Score STANDARD — Atenção")

    else:
        st.error("🔴 Score POOR — Cliente não aprovado")

    st.write(f"Classificação do modelo: {resultado}")

    # Mostrar dados usados
    st.write("Dados utilizados:")
    st.dataframe(dados)

st.divider()

# Sobre o projeto
st.subheader("Sobre o projeto")

st.markdown("""
Projeto desenvolvido com:

- Python
- Pandas
- Scikit-Learn
- Streamlit
- Machine Learning

Objetivo:
Prever score de crédito com base em informações financeiras do cliente.
""")