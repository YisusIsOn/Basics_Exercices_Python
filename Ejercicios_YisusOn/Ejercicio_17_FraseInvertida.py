"Ejercicio 18"

"""
Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, 
y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
"""
"Modo Basico"

print("\n")
print("".center(50,"-"))
frase =input("Ingrese una frase: ")
frase_Invertida = frase[::-1]
print("La frase invertida es: " + frase_Invertida)
print("".center(50,"-"))
print("\n")