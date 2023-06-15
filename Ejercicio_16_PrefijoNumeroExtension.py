"Ejercicio 16"

"""
Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, 
y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este formato 
y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
"""

"Intentare hacer un codigo mas basico para este ejercicio"

print("\n")
print("".center(50,"-"))
user_Phone = input("Ingrese su numero telefonico con el formato prefijo-número-extension: ")
UsPh = [user_Phone]
prefijo = user_Phone.split("-")[0]
numero = user_Phone.split("-")[1]
extension = user_Phone.split("-")[2]

print("El numero de telefono es: " + numero +"\n")