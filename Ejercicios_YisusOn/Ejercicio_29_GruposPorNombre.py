"Ejercicio 29"

"""
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. 
Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
"""
"Basico"

print("\n")

nombre = input("Ingrese su nombre: ")
sexo = input("Ingrese su sexo (M o H): ")

primeraLetra_Nombre = nombre[0]

if primeraLetra_Nombre.upper() < "M" and sexo.lower() == "m":
    print("Usted pertenece al grupo A")

elif primeraLetra_Nombre.upper() > "N" and sexo.lower() == "h":
    print("Usted pertenece al grupo A")
else:
    print("Usted pertenece al grupo B")


