"Ejercicio 11"

"""
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. 
Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. 
Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales. 
"""

def user_Deposit():
    print("\n")
    print("CALCULADORA DEL 4% DE LA CUENTA EN TRES AÑOS".center(50))
    print("".center(50,"-"))
    deposit = float(input("Ingrese el monto a depositar: "))
    return deposit

def calculo(deposit):
    first_Year = deposit * (1 + 0.04)
    second_Year = first_Year * (1 + 0.04)
    third_Year = second_Year * (1 + 0.04)
    return first_Year, second_Year, third_Year

def print_calculo(first_Year, second_Year, third_Year):
    print("".center(50,"-"))
    print(f"El primer año obtienes : {first_Year:.2f}")
    print(f"El segundo año obtienes: {second_Year:.2f}")
    print(f"El tercer año obtienes : {third_Year:.2f}")
    print("\n")

if __name__ == "__main__":
    deposit = user_Deposit()
    first_Year, second_Year, third_Year = calculo(deposit)
    print_calculo(first_Year, second_Year, third_Year)