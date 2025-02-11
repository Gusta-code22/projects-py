import streamlit as st
import pandas as pd
import os

# Verifica se o arquivo CSV existe
if os.path.exists('Produtos.csv'):
    df = pd.read_csv('Produtos.csv')
else:
    df = pd.DataFrame(columns=['nome', 'preco'])

# Título da aplicação
st.title(f'Cadastro de produtos')

# Exibe o DataFrame na barra lateral
if st.sidebar.button('Ver Produtos cadastrados'):
    st.sidebar.dataframe(df)

# Formulário para cadastrar o produto
with st.form(key='Preco e nome'):
    nome = st.text_input(f'Insira o nome do produto que deseja cadastrar: ')
    preco = st.number_input(f'Preço do Produto: ', min_value=0.00, format='%2f')
    
    # Botão para cadastrar o produto
    botao_sair = st.form_submit_button('Cadastrar Produto')
    
    if botao_sair:
        # Adiciona o novo produto ao DataFrame
        novo_produto = {'nome': nome, 'preco': preco}
        df_novo_produto = pd.DataFrame([novo_produto])

        # Garantir que o novo DataFrame tem as mesmas colunas que o original
        df_novo_produto = df_novo_produto[['nome', 'preco']]

        # Concatena o novo produto ao DataFrame existente
        df = pd.concat([df, df_novo_produto], ignore_index=True)

        # Salva o DataFrame no arquivo CSV
        df.to_csv('Produtos.csv', index=False)

        # Exibe o DataFrame atualizado na página principal
        st.dataframe(df)
        