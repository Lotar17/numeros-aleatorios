from math import exp
import matplotlib.pyplot as plt

from numpy import empty, float64, log, ndarray, linspace


class Exponencial:
    def __init__(self, alfa=2, x=1) -> None:
        self.alfa = alfa
        self.x = x

    def densidad(self, x):
        return self.alfa * exp(-self.alfa * x)

    def acumulativa(self, x):
        return 1 - exp(-self.alfa * x)

    def media(self):
        return 1 / self.alfa

    def varianza(self):
        return self.media() ** 2

    def exponencial_valores(self, r: ndarray):
        media = self.media()
        valores = empty(len(r), dtype=float64)
        for i in range(len(r)):
            valores[i] = -media * log(r[i])
        return valores

    def graficar(self):
        x = linspace(0, self.x)
        y = empty(len(x), dtype=float64)
        for i in range(len(x)):
            y[i] = self.densidad(x[i])
        plt.figure(figsize=(10, 5))
        plt.subplot(121)
        plt.plot(x, y)
        plt.title("Funcion densidad")
        for i in range(len(x)):
            y[i] = self.acumulativa(x[i])
        plt.subplot(122)
        plt.plot(x, y)
        plt.title("Funcion acumulativa")
        plt.show()
