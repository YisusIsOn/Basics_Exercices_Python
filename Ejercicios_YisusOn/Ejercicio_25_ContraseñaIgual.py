"Ejercicio 25"

"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida 
por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
"""
"Basico"

contraseña_Guardada = "hola"

ingreso_Contraseña = input("Ingrese la contraseña: ")

if ingreso_Contraseña == contraseña_Guardada.lower():
    print("La contraseña es correcta")
else:
    print("La contraseña es incorrecta")