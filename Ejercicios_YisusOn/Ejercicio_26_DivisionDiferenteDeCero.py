"Ejercicio 26"

"""
Escribir un programa que pida al usuario dos números y muestre por pantalla su división.
 Si el divisor es cero el programa debe mostrar un error.
"""
"Basico"

print("\n")
numero_Uno = float(input("Ingrese el dividendo: "))
numero_Dos = float(input("Ingrese el divisor: "))

if numero_Dos == 0:
    print("El divisior es 0, eso genera una indeterminacion")
else:
    division = numero_Uno/numero_Dos
    print("La division es = " + str(division))