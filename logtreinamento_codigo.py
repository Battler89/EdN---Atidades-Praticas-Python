# Programa para calcular dados de um arquivo .csv
import pandas as pd
import numpy as np
#    arquivo = "logstreinamento_dados.csv"
#    frame = pd.read_csv(arquivo)
#    if 'tempo_processamento' not in frame.columns:
#        raise ValueError("A coluna 'tempo_processamento'")
#    media = frame['tempo_processamento'].mean()
#    desvio_padrao = frame['tempo_processamento'].std()
#    print(f"Média do tempo de execução: {media:.2f}")
#    print(f"Desvio padrão do tempo de execução: {desvio_padrao:.2f}")
try:
    df = pd.read_csv("logtreinamento_dados.csv")
    media = df["tempo_processamento"].mean()
    desvio_padrao = df["tempo_processamento"].std()
    print(f"Média do tempo de execução: {media:.2f}")
    print(f"Desvio padrão do tempo de execução: {desvio_padrao:.2f}")
except FileNotFoundError:
    print(f"Erro, o arquivo não foi encontrado")
except ValueError as e:
    print(f"Erro: {e}")
except Exception as e:
    print(f"Erro inesperado: {e}")
