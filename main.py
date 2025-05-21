from distribuciones import Exponencial
import generadores
import test

from tests import (
    frequency_monobit_test,
    runs_test,
    test_de_frecuencia_por_bloque,
    transformada_discreta_de_fourier,
)

"""    
CANTIDAD_DE_NUMEROS_A_GENERAR = 250000
SEMILLA = 9731
CICLOS = 10


lista_numeros_cuadrados = []
lista_numeros_cuadrados_bits = ""

lista_numeros_rand = []
lista_numeros_rand_bits = ""

lista_numeros_randu = []
lista_numeros_randu_bits = ""

semilla_cuadrados = SEMILLA
semilla_rand = SEMILLA
semilla_randu = SEMILLA

for _ in range(CANTIDAD_DE_NUMEROS_A_GENERAR):
    semilla_cuadrados = generadores.generador_metodo_cuadrados(
        semilla_cuadrados, CICLOS
    )
    lista_numeros_cuadrados.append(semilla_cuadrados)
    lista_numeros_cuadrados_bits += bin(semilla_cuadrados)[2:]

    semilla_rand = generadores.generador_rand(semilla_rand, CICLOS)
    lista_numeros_rand.append(semilla_rand)
    lista_numeros_rand_bits += bin(semilla_rand)[2:]

    semilla_randu = generadores.generador_randu(semilla_randu, CICLOS)
    lista_numeros_randu.append(semilla_randu)
    lista_numeros_randu_bits += bin(semilla_randu)[2:]


print("TEST 1: Frecuencia de monobit")
print("TEST 2: Frecuencia de bloques")
print("TEST 3: Runs Test")
print("TEST 4: Transformada discreta de fourier")

resultado_cuadrado_test1 = frequency_monobit_test(lista_numeros_cuadrados_bits)
resultado_cuadrado_test2 = test_de_frecuencia_por_bloque(lista_numeros_cuadrados_bits)
resultado_cuadrado_test3 = runs_test(lista_numeros_cuadrados_bits)
resultado_cuadrado_test4 = transformada_discreta_de_fourier(
    lista_numeros_cuadrados_bits
)

resultado_rand_test_1 = frequency_monobit_test(lista_numeros_rand_bits)
resultado_rand_test_2 = test_de_frecuencia_por_bloque(lista_numeros_rand_bits)
resultado_rand_test_3 = runs_test(lista_numeros_rand_bits)
resultado_rand_test_4 = transformada_discreta_de_fourier(lista_numeros_rand_bits)


resultado_randu_test_1 = frequency_monobit_test(lista_numeros_randu_bits)
resultado_randu_test_2 = test_de_frecuencia_por_bloque(lista_numeros_randu_bits)
resultado_randu_test_3 = runs_test(lista_numeros_randu_bits)
resultado_randu_test_4 = transformada_discreta_de_fourier(lista_numeros_randu_bits)

print(
    f"Metodo de los cuadrados: TEST 1: {resultado_cuadrado_test1} TEST 2: {resultado_cuadrado_test2} TEST3: {resultado_cuadrado_test3} TEST4: {resultado_cuadrado_test4}"
)

print(
    f"GCL: rand : TEST 1: {resultado_rand_test_1} TEST 2: {resultado_rand_test_2} TEST3: {resultado_rand_test_3} TEST4: {resultado_rand_test_4}"
)

print(
    f"GCL: RANDU : TEST 1: {resultado_randu_test_1} TEST 2: {resultado_randu_test_2} TEST3: {resultado_randu_test_3} TEST4: {resultado_randu_test_4}"
)
"""

sucesion_rand = generadores.generador_rand(10)
for numero in sucesion_rand:
    print(numero)
print("RANDU")
sucesion_randu = generadores.generador_randu(200)
for numero in sucesion_randu:
    print(numero)
print("CUADRADOS")
sucesion_cuadrados = generadores.generador_metodo_cuadrados(10)
for numero in sucesion_cuadrados:
    print(numero)

print("CREO EL OBJETO EXPONENCIAL")
e = Exponencial()
valores_exponenciales = e.exponencial_valores(sucesion_randu)
e.graficar(valores_exponenciales)
