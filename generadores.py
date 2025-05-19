import numpy as np


def generador_metodo_cuadrados(n=1500, semilla=9731):
    """
    Genera n valores pseudoaleatorios en (0,1)
    usando el método de cuadrados medios de 4 dígitos.
    """
    x = np.empty(n, dtype=np.int64)
    u = np.empty(n, dtype=np.float64)

    semilla = semilla % 10000
    x[0] = semilla
    u[0] = semilla / 10000

    for i in range(1, n):
        cuadrado = x[i - 1] * x[i - 1]
        s = str(cuadrado).zfill(8)
        semilla_nueva = int(s[2:6])
        x[i] = semilla_nueva
        u[i] = semilla_nueva / 10000

    return u


def generador_rand(n=1500, semilla=None):
    m = 2**31 - 1
    a = 7**5  # 16807
    if semilla is None:
        semilla = np.random.randint(0, m)
    x = np.empty(n, dtype=np.int64)
    u = np.empty(n, dtype=np.float64)
    x[0] = semilla
    u[0] = x[0] / m  # transformamos al (0,1)
    for i in range(1, n):
        x[i] = (a * x[i - 1]) % m
        u[i] = x[i] / m
    return u


def generador_randu(n=1500, semilla=None):
    m = 2**31
    a = 2**16 + 3
    if semilla is None:
        semilla = np.random.randint(0, m)
    x = np.empty(n, dtype=np.int64)
    u = np.empty(n, dtype=np.float64)
    x[0] = semilla
    u[0] = x[0] / m  # transformamos al (0,1)
    for i in range(1, n):
        x[i] = (a * x[i - 1]) % m
        u[i] = x[i] / m
    return u
