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


def generador_randu(semilla: int, ciclos: int):
    for _ in range(ciclos):
        semilla = (2**16 + 3) * semilla % (2**31)
    return semilla


def generador_rand(semilla: int, ciclos: int):
    for _ in range(ciclos):
        semilla = (7**5) * semilla % (2**31 - 1)
    return semilla
