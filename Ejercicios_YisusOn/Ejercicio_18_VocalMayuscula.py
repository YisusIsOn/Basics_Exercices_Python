"Ejercicio 18"

"""
Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, 
y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
"""
"Modo Basico"

print("\n")
print("".center(50, "-"))

frase = input("Ingrese una frase: ")
vocal = input("Ingrese una vocal: ")
vocal_lower = vocal.lower()

conjunto_vocal =['a', 'e', 'i', 'o', 'u']

if len(vocal) == 1 and vocal_lower in conjunto_vocal:
    print(frase.replace(vocal, vocal.upper()))

else:
    print("Error Ingrese una vocal")

