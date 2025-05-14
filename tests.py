from math import erfc, isqrt, sqrt
import re
from scipy.stats import chi2


def frequency_monobit_test(numeros: str):
    """
    NIST recomienda una secuencia de 0 y 1 mayor
    o igual a 100
    """
    n = len(numeros)
    numeros_transformados = numeros.replace("0", "-1")
    tokens = re.findall(r"-?1", numeros_transformados)
    lista_transformada = list(map(int, tokens))
    for numero in lista_transformada:
        print(numero)
    total = sum(lista_transformada)
    print("Total: ", total)
    solucion_obs = abs(total) / sqrt(n)
    p_value = erfc(solucion_obs / sqrt(2))
    return p_value >= 0.1


def test_de_frecuencia_por_bloque(numeros: str):
    """
    NIST recomiena al menos 100 bits, es decir, se recomienda que
    el parámetro numeros >= 100 y que el tamaño_bloque >= 20
    """
    n = len(numeros)
    divisores = set()
    limite = int(isqrt(n))
    for i in range(1, limite + 1):
        if n % i == 0:
            divisores.add(i)
            divisores.add(n // i)
    print("Valores de tamaño_bloque posibles: ", sorted(divisores))
    tamaño_bloque = int(input("Ingrese un valor posible del tamaño de bloque: "))
    bloques = [numeros[i : i + tamaño_bloque] for i in range(0, n, tamaño_bloque)]
    proporcion_de_unos_por_bloque = []
    for bloque in bloques:
        proporcion_de_unos_por_bloque.append(
            round(bloque.count("1") / tamaño_bloque, 1)
        )
    print(proporcion_de_unos_por_bloque)
    proporcion_convertida = list(
        map(lambda x: (x - 0.5) ** 2, proporcion_de_unos_por_bloque)
    )
    print(proporcion_convertida)
    chi_cuadrado = 4 * tamaño_bloque * sum(proporcion_convertida)
    p_value = chi2.sf(chi_cuadrado, len(bloques) - 1)
    return p_value >= 0.01


def runs_test(numeros: str):
    n = len(numeros)
    cantidad_de_unos = numeros.count("1")
    frecuencia_pre_test = cantidad_de_unos / n
    tao = 2 / sqrt(n)
    sumatoria = 1
    if abs(frecuencia_pre_test - 0.5) < tao:
        for numeroActual, numeroSiguiente in zip(numeros, numeros[1:]):
            if numeroActual != numeroSiguiente:
                sumatoria += 1
        dividendo = abs(
            sumatoria - 2 * n * frecuencia_pre_test * (1 - frecuencia_pre_test)
        )
        divisor = 2 * sqrt(2 * n) * frecuencia_pre_test * (1 - frecuencia_pre_test)
        p_value = erfc(dividendo / divisor)
        return p_value >= 0.01
    return False
