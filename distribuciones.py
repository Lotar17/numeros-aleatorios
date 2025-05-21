from math import exp

from numpy import empty, float64, log, ndarray


class exponencial:
    def __init__(self, alfa=2, x=1) -> None:
        self.alfa = alfa
        self.x = x

    def densidad(self):
        return self.alfa * exp(-self.alfa * self.x)

    def acumulativa(self):
        return 1 - exp(-self.alfa * self.x)

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
