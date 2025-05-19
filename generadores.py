import numpy as np


def generador_metodo_cuadrados(semilla: int, n: int) -> int:
    """
    Ejecuta n iteraciones del método de cuadrados medios
    y devuelve solo la semilla resultante al final.
    """
    for _ in range(n):
        x = semilla * semilla
        if x >= 100:
            semilla = (x // 100) % 10000
        else:
            semilla = 0
    return semilla


def generador_rand(n=1500, semilla=None):
    m = 2**31 - 1
    a = 7**5  # 16807
    if semilla is None:
        semilla = np.random.randint(0, m)
    x = np.empty(n, dtype=np.int64)
    u = np.empty(n, dtype=np.float64)
    x[0] = semilla
    u[0] = x[0] / m
    for i in range(1, n):
        x[i] = (a * x[i - 1]) % m
        u[i] = x[i] / m
    return u


def generador_randu(semilla: int, ciclos: int):
    for _ in range(ciclos):
        semilla = (7**5) * semilla % (2**31 - 1)
    return semilla
