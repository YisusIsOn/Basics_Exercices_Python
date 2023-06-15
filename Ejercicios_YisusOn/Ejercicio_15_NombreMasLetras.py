"Ejercicio 15"

"""
Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca 
muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.
"""


def datos_Ingresados():
    print("\n")
    print("".center(50, "-"))
    user_Name = input("Introduzca su nombre: ")
    return user_Name

def arreglo_Nombre (user_Name):
    username_Sinespacios = user_Name.replace(" ", "")
    mayus_Username = user_Name.upper()
    cantidadletras_Username =  len(username_Sinespacios)
    return mayus_Username, cantidadletras_Username

def salida_Username(mayus_Username, cantidadletras_Username, user_Name):
    print("\n")
    print("".center(50, "-"))
    print(str(user_Name) +" tiene " + str(cantidadletras_Username) + " letras, donde " + str(mayus_Username) + " es el nombre de usuario en mayúsculas y " + str(cantidadletras_Username) + " es el número de letras que tienen el nombre.")

if __name__ == "__main__":
    user_Name = datos_Ingresados()
    mayus_Username, cantidadletras_Username = arreglo_Nombre (user_Name)
    salida_Username(mayus_Username, cantidadletras_Username, user_Name)