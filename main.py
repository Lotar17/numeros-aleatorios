import tests

numero = int(input("Ingrese un numero: "))

numero_binario = bin(numero)[2:]
print("Numero en binario", numero_binario, "Longitud:", len(numero_binario))


tests.test_de_frecuencia_por_bloque(numero_binario)
