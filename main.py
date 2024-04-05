import streamlit as st
import pandas as pd
import plotly.express as px

# Criar botão de upload para o arquivo CSV
uploaded_file = st.file_uploader("Escolha um arquivo em CSV", type=['csv'])

# Verificar se o arquivo foi carregado pelo usuário
if uploaded_file is not None:
    # Carregar os dados do CSV
    data = pd.read_csv(uploaded_file, decimal=',')

    # Exibir os nomes das colunas na página
    st.write("Nomes das colunas no arquivo CSV:")
    st.write(data.columns.tolist())  # Lista os nomes das colunas

    # Verificar se as colunas corretas estão presentes no DataFrame
    required_columns = ["Amount Spent", "CPC (Cost per Link Click)", "Link Clicks",
                        "Cost per Messaging Conversations Started", "Messaging Conversations Started"]
    missing_columns = [col for col in required_columns if col not in data.columns]

    if not missing_columns:

        # Gráfico interativo para Alcance vs. Valor Gasto
        fig_reach = px.histogram(data, x="Amount Spent", y="Reach", title='Alcance x Valor Gasto', nbins=20, labels={'Amount Spent': 'Valor Gasto', 'Reach': 'Alcance'})
        fig_reach.update_xaxes(tickformat=".2f")  # Define o formato dos valores no eixo X
        fig_reach.update_yaxes(tickformat=",")  # Define o formato dos valores no eixo Y
        fig_reach.update_traces(texttemplate='%{y}', textposition='outside')  # Adiciona o valor gasto como rótulo nas barras
        st.plotly_chart(fig_reach)

        # Gráfico interativo para Cliques e custo por clique
        fig_click = px.histogram(data, x="CPC (Cost per Link Click)", y="Link Clicks", title='Cliques e custo por clique', nbins=20, labels={'CPC (Cost per Link Click)': 'Custo por Clique', 'Link Clicks': 'Cliques'})
        fig_click.update_xaxes(tickformat=".2f")  # Define o formato dos valores no eixo X
        fig_click.update_yaxes(tickformat=",")  # Define o formato dos valores no eixo Y
        fig_click.update_traces(texttemplate='%{y}', textposition='outside')  # Adiciona o valor gasto como rótulo nas barras
        st.plotly_chart(fig_click)

        # Gráfico interativo para Mensagem e custo por mensagem
        fig_mensage = px.histogram(data, x="Cost per Messaging Conversations Started", y="Messaging Conversations Started", title='Mensagem e custo por mensagem', nbins=20, labels={'Cost per Messaging Conversations Started': 'Custo por Mensagem', 'Messaging Conversations Started': 'Mensagem'})
        fig_mensage.update_xaxes(tickformat= ".2f") # Define o formato dos valores no eixo x
        fig_mensage.update_yaxes(tickformat=",")  # Define o formato dos valores no eixo y
        fig_mensage.update_traces(texttemplate='%{y}', textposition='outside')  # Adiciona o valor gasto como rótulo nas barras
        st.plotly_chart(fig_mensage)
    else:
        st.write(f"As colunas necessárias {missing_columns} não foram encontradas no arquivo CSV.")
else:
    st.write("Nenhum arquivo selecionado. Por favor, faça o upload de um arquivo CSV.")
