from math import erfc, sqrt
import re


def frequency_monobit_test(numeros: str):
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
