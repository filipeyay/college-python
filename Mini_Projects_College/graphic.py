import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

date = {
    "year": [2018, 2019, 2020, 2021, 2022, 2023],
    "expenses": [100, 154, 300, 200, 400, 150],
}

df = pd.DataFrame(data)


class TimeSeries:
    def __init__(self, df):
        self.df = df

    def plot(self):
        plt.figure(figsize=(10, 6))
        plt.plot(self.df["year"], self.df["expenses"], marker="o")
        plt.xlabel("Year")
        plt.ylabel("Expenses")
        plt.title("Expense Time Series")
        plt.grid(True)
        plt.show()

    def linear_regression(self):
        x = self.df["year"].values.reshape(-1, 1)
        y = self.df["expenses"].values

        model = LinearRegression()
        model.fit(x, y)

        plt.figure(figsize=(10, 6))
        plt.plot(x, y, marker="o", label="Expenses Data")
        plt.plot(
            x, model.predict(x), color="red", linestyle="--", label="Linear Regression"
        )
        plt.xlabel("Year")
        plt.ylabel("Expenses")
        plt.title("Expense Time Series Linear Regression")
        plt.legend()
        plt.grid(True)
        plt.show()


time_series = TimeSeries(df)
time_series.plot()
time_series.linear_regression()
