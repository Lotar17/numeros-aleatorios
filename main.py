import tests

numero = int(input("Ingrese un numero: "))

numero_binario = bin(numero)[2:]
print(numero_binario, "Longitud: ]", len(numero_binario))


tests.frequency_monobit_test(numero_binario)
