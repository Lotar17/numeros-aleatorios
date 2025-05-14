import tests

numero = int(input("Ingrese un numero: "))

numero_binario = bin(numero)[2:]
print("Numero en binario", numero_binario, "Longitud:", len(numero_binario))

print(tests.runs_test(numero_binario))
