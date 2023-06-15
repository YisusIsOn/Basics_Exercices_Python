"Ejercicio 14"

"""
Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces,
 una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. 
 El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.
"""

def initial_Dates():
    print("\n")
    print("".center(50,"-"))

    user_Name = str(input("Ingrese su nombre completo: "))
    print("".center(50,"-"))
    print("\n")
    for i in range(1):
       print("Su nombre en minusculas: " +user_Name.lower())
       print("Su nombre en mayusculas: " +user_Name.upper())
       print("Su nombre formal: " +user_Name.title() +"\n")
    
if __name__=="__main__": 
    initial_Dates()

