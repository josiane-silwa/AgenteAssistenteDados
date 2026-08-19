## 🦜 Analysis - Assistente de análise de dados com IA
<img width="1919" height="974" alt="Captura de tela 2026-08-19 171741" src="https://github.com/user-attachments/assets/6ed6c447-881b-4c80-bb8a-45795063d181" />


## 📋 Descrição
Projeto desenvolvido para o Challenge Alura Agente, do programa ONE AI - TECH AI BUILDER. Que implementa uma aplicação Python, com a construção de um Agente de IA que responde perguntas de um colaborador da área de dados de uma empresa fictícia. Auxiliando-o na análise dos dados.

## 🛠️ Tecnologias Utilizadas
<div align="left">
    
[![Minhas Habilidades](https://skillicons.dev/icons?i=python,git
)](https://skillicons.dev) <img width="50" height="50" alt="LangChain-Logo" src="https://github.com/user-attachments/assets/7fbfe4ae-c187-4d3d-b862-a85a4197f124" />
<img width="60" height="60" alt="streamlit-icon" src="https://github.com/user-attachments/assets/99fee66a-8d0b-496a-bfb6-e91fbc927889" />

  </div>

## 🔧 Requisitos
    langchain==0.3.22
    langchain-groq==0.3.2
    langchain-core==0.3.50
    langchain-experimental==0.3.4
    langchain-community==0.3.20
    pandas==2.2.3
    tabulate==0.9.0
    streamlit==1.44.1
    matplotlib==3.10.1
    seaborn==0.13.2
    python-dotenv==1.0.1

## 🏗️📐 Arquitetura
    AgenteAssistenteDados/
    ├── documentos/
    │   └── dados_entrega_modificado.csv     # Dataframe de dados
    ├── App.py                               # Interface de chat (Streamlit)
    ├── ferramentas.py                       # Construção das ferramentas - Orquestração - Geração de respostas
    ├── requirements.txt
    ├── README.md
    └── .env
    
## 📦 Instalação
Siga os passos abaixo para rodar o projeto localmente:

    Clone o repositório:
      git clone https://github.com/jandsonrj/pokemon-ionic-app.git

    Acesse o diretório do projeto:
     cd AgenteAssistenteDados

    Instale as dependências:
      pip install -r requirements.txt

    Inicie a aplicação:
      streamlit run .\App.py
    
A aplicação será automaticamente aberta no seu navegador na porta: http://localhost:8501/
<br><br>

## 📁 Acesso ao projeto
<a href="https://agenteassistentedados.streamlit.app" target="_blank"><span>Clique aqui</span></a> para ver uma demonstração do projeto rodando no Streamlit.


## 🔎❓Exemplos de consultas, perguntas e respostas
Para iniciarmos o agente, devemos fazer o upload do arquivo dados_entregas_modificado.csv
<br>
<img width="1919" height="974" alt="Captura de tela 2026-08-19 171741" src="https://github.com/user-attachments/assets/0a1dc5d7-678d-4c5a-902c-66355d62a28a" />
<img width="1919" height="967" alt="Captura de tela 2026-08-19 192951" src="https://github.com/user-attachments/assets/31c87d0b-358b-446c-a665-d221a6df5739" />
<img width="1916" height="1037" alt="Captura de tela 2026-08-17 025014" src="https://github.com/user-attachments/assets/dd4fd4d9-7f15-49dd-b58d-2f34e5a1f2cc" />
<img width="1919" height="1027" alt="Captura de tela 2026-08-17 025047" src="https://github.com/user-attachments/assets/cf1a4f36-0afb-4c57-ab7c-fc2fc96949f4" />
<br><br>
# 🔎 Exemplo de pergunta sobre os dados:
🔎 Qual é a média do tempo de entrega?
<img width="1916" height="1014" alt="Captura de tela 2026-08-17 025134" src="https://github.com/user-attachments/assets/a401a2e1-bbec-4d55-9e0e-02f3cd326104" />
<br><br>
🔎 Crie um gráfico da média de tempo de entrega por clima:
<br>
<img width="1919" height="1018" alt="Captura de tela 2026-08-17 025214" src="https://github.com/user-attachments/assets/b497bbdd-94c4-44a9-b53e-048d388f3454" />
