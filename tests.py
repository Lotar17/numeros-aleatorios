from math import erfc, isqrt, sqrt
import re
from numpy import fft
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
    total = sum(lista_transformada)
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
    proporcion_convertida = list(
        map(lambda x: (x - 0.5) ** 2, proporcion_de_unos_por_bloque)
    )
    chi_cuadrado = 4 * tamaño_bloque * sum(proporcion_convertida)
    p_value = chi2.sf(chi_cuadrado, len(bloques) - 1)
    return p_value >= 0.01


def runs_test(numeros: str):
    """
    NIST recomienda que la cantidad de bits sea mayor o igual a 100,
    es decir, que len(numeros) >= 100
    """
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


def transformada_discreta_de_fourier(numeros: str):
    """
    NIST recomienda como mínimo 100 bits, es decir,
    len(numeros) >= 100
    """
    n = len(numeros)
    numeros_transformados = numeros.replace("0", "-1")
    tokens = re.findall(r"-?1", numeros_transformados)
    lista_transformada = list(map(int, tokens))
    s = fft.fft(lista_transformada)
    n2 = len(s)
    # Tomar los primeros n/2 elementos
    S_prime = s[: n2 // 2]
    # Calcular la magnitud de cada componente
    m = abs(S_prime)

    # Descartar el componente de frecuencia cero ya que ese primer coeficiente refleja simplemente el sesgo global, no un patrón periódico “real” a ninguna frecuencia.
    m_true_peaks = m[1:]
    t = sqrt(2.995732274 * n)
    n0 = 0.95 * n / 2
    n1 = 0
    for valor in m_true_peaks:
        if valor < t:
            n1 += 1
    d = (n1 - n0) / sqrt(n * 0.95 * 0.05 / 2)
    p_value = erfc(abs(d) / sqrt(2))
    return p_value >= 0.01
