
# Bibliotecas importadas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# (1) Entrada de dados
data = {
    'ano': [2018, 2019, 2020, 2021, 2022, 2023],
    'despesas': [100, 154, 300, 200, 400, 150]
}

df = pd.DataFrame(data)

# (2) Classe para tratar séries temporais de despesas
class TimeSeries:
    def __init__(self, df):
        self.df = df

    def plot(self):
        plt.figure(figsize=(10, 6))
        plt.plot(self.df['ano'], self.df['despesas'], marker='o')
        plt.xlabel('Ano')
        plt.ylabel('Despesas')
        plt.title('Série Temporal de Despesas')
        plt.grid(True)
        plt.show()

    def linear_regression(self):
        X = self.df['ano'].values.reshape(-1, 1)
        y = self.df['despesas'].values

        model = LinearRegression()
        model.fit(X, y)

        plt.figure(figsize=(10, 6))
        plt.plot(X, y, marker='o', label='Dados de Despesas')
        plt.plot(X, model.predict(X), color='red', linestyle='--', label='Regressão Linear')
        plt.xlabel('Ano')
        plt.ylabel('Despesas')
        plt.title('Regressão Linear em Séries Temporais de Despesas')
        plt.legend()
        plt.grid(True)
        plt.show()

# (3) Classe para gerar gráficos de linha e de regressão linear
time_series = TimeSeries(df)

# Visualizar linha de despesas
time_series.plot()

# Mostrar regressão
time_series.linear_regression()
