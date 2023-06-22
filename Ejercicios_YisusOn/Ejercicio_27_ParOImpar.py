"Ejercicio 27"

"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
"""
"Basico"

print("\n")
numero = int(input("Ingrese un numero: "))

resto = numero % 2

if resto == 0:
    print("El numero " + str(numero) + " es par")
else:
    print("El numero " + str(numero) + " es impar")