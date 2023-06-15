"Ejercicio 13"

"""
Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas 
el nombre del usuario tantas veces como el número introducido.
"""

def initial_Dates():
    print("\n")
    print("".center(50,"-"))

    user_Name = str(input("Ingrese su nombre: "))
    integer_Number = int(input("Ingrese un numero entero: "))
    print("".center(50,"-"))
    print("\n")
    return user_Name, integer_Number

def bucle_ofName (user_Name, integer_Number):
    for i in range(integer_Number) :
       print(user_Name +"\n")
       

if __name__=="__main__": 
    user_Name, integer_Number = initial_Dates()
    bucle_ofName (user_Name, integer_Number)