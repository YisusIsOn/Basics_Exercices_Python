"Ejercicio 21"

"""
Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa 
y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que 
también funcione cuando el día o el mes se introduzcan con un solo carácter.
"""

def ingreso_Datos():
    print("\n")
    print("FECHA DE NACIMIENTO".center(70))
    print("".center(70, "-"))
    date_OfBorn = input("Ingrese su fecha de nacimiento en el formato dd/mm/aaa:  ")
    print("".center(70, "-"))
    return date_OfBorn

def div_Format(date_OfBorn):
    day = date_OfBorn.split("/")[0]
    month = date_OfBorn.split("/")[1]
    age = date_OfBorn.split("/")[2]
    return day, month, age

def user_Out(day, month, age):
    print("El dia es: {}".format(day).center(70))
    print("El mes es: {}".format(month).center(70))
    print("El año es: {}".format(age).center(70))
    print("".center(70, "-"))
    print("\n")

if __name__ == "__main__":
    date_OfBorn = ingreso_Datos()
    day, month, age = div_Format(date_OfBorn)
    user_Out(day, month, age)