import streamlit as st
import pandas as pd
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.agents import create_react_agent
from langchain.agents import AgentExecutor
from ferramentas import criar_ferramentas
import os

# Inicia o app
st.set_page_config(page_title="Agente Assistente de Dados com IA", layout="centered")
st.title("🦜 Agente Assistente de análise de dados com IA")

# Descrição da ferramenta
st.info("""
Este assistente utiliza um agente, criado com Langchain, para te ajudar a explorar, analisar e visualizar dados de forma interativa.
Faça o upload de um arquivo CSV e você poderá:

- 📄 **Gerar relatórios automáticos**:
    - **Relatório de informações gerais**: apresenta a dimensão do DataFrame, nomes e tipos das colunas, contagem de dados nulos e duplicados, além de sugestões de tratamentos e análises adicionais.
    - **Relatório de estatísticas descritivas**: exibe valores como média, mediana, desvio padrão, mínimo e máximo; identifica possíveis outliers e sugere próximos passos com base nos padrões detectados.

- 🔎 **Fazer perguntas simples sobre os dados**: como "Qual é a média do tempo de entrega?", "Quantos registros existem para cada categoria?", ou "Qual é o valor máximo da coluna de vendas?".
                
- 📊 **Criar gráficos automaticamente** com base em perguntas em linguagem natural.

Ideal para analistas, cientistas de dados e equipes que buscam agilidade e insights rápidos com apoio de IA.
""")

# Upload do CSV
st.markdown("### 📁 Faça upload do seu arquivo CSV")
arquivo_carregado = st.file_uploader("Selecione um arquivo CSV", type="csv", label_visibility="collapsed")

if arquivo_carregado:
    df = pd.read_csv(arquivo_carregado)
    st.success("Arquivo carregado com sucesso!")
    st.markdown("### 🔍 Primeiras linhas do DataFrame")
    st.dataframe(df.head())

    # LLM
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    llm = ChatGroq(
        api_key=GROQ_API_KEY,
        model_name="llama-3.3-70b-versatile",
        temperature=0
    )

    # Ferramentas
    tools = criar_ferramentas(df)