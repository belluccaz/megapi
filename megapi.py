import pandas as pd
from datetime import datetime
import streamlit as st

@st.cache_data
def processar_numeros(numeros_usuario):
    # Carregar dados
    df = pd.read_csv("megasena.csv")

    # Selecionar apenas as colunas para comparação
    colunas_bolas = ['Bola1', 'Bola2', 'Bola3', 'Bola4', 'Bola5', 'Bola6']

    # Inicializar uma lista para armazenar as linhas que atendem ao critério
    linhas_selecionadas = []

    for indice, linha in df.iterrows():
        numeros_sorteados = linha[colunas_bolas].tolist()
        numeros_em_comum = set(numeros_usuario).intersection(numeros_sorteados)
        if len(numeros_em_comum) >= 4:
            linhas_selecionadas.append(linha)
    return linhas_selecionadas

# Interface do Streamlit
def main():
    st.title('Análise Megasena')
    
    # Solicitar ao usuário os números desejados
    numeros_usuario = st.text_input("Informe os números que deseja analisar, separados por vírgula:")
    numeros_usuario = [int(numero.strip()) for numero in numeros_usuario.split(',') if numero.strip()]

    if numeros_usuario:
        linhas_selecionadas = processar_numeros(numeros_usuario)

        # Exibir resultados
        if linhas_selecionadas:
            st.write("Quatro ou mais dessas dezenas já foram sorteadas nos seguintes concursos:")
            # Converter as linhas selecionadas para um DataFrame
            df_linhas_selecionadas = pd.DataFrame(linhas_selecionadas)
            st.write(df_linhas_selecionadas)
        else:
            st.write("Nenhuma linha encontrada com os critérios especificados.")

if __name__ == "__main__":
    main()
