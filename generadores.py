def generador_metodo_cuadrados(seed: int, n: int) -> int:
    """
    Ejecuta n iteraciones del método de cuadrados medios
    y devuelve solo la semilla resultante al final.
    """
    for _ in range(n):
        x = seed * seed
        if x >= 100:
            seed = (x // 100) % 10000
        else:
            seed = 0
    return seed
