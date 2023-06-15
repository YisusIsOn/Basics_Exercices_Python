"Ejercicio 9"
"Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual" 
"y el número de años, y muestre por pantalla el capital obtenido en la inversión."

def user_Dates():
    print("\n")
    investor=float(input("Ingrese la cantidad a invertir: "))
    interes=float(input("Ingrese el interes anual en %: "))
    number_Ages=int(input("Ingrese el numero de años: "))
    return investor, interes, number_Ages

def obtain_Capital (investor, interes, number_Ages):
    porcentain = interes / 100
    interes_Simple = investor * (1 + porcentain * number_Ages)
    interes_Compuest = investor * (1 + porcentain)**number_Ages
    return interes_Simple, interes_Compuest

def print_Capital(investor, interes, number_Ages, interes_Simple, interes_Compuest):
    print("\n")
    print(f"Con un capital de {investor:,.0f} un interés de {interes:.0f}% y un tiempo de {number_Ages} años")
    print(f"Obtienes un capital de {interes_Simple:,.0f} con el interes simple")
    print(f"Obtienes un capital de {interes_Compuest:,.0f} con el interes compuesto")
    print("\n")
    print("Factura:".center(50))
    print("".center(50,"-"))
    print(f"Capital inicial: ${investor:,.0f}".center(50))
    print(f"Tasa de interés: {interes:.0f}%".center(50))
    print(f"Número de años: {number_Ages}".center(50))
    print("".center(50,"-"))
    print(f"Capital con interés simple: ${interes_Simple:,.0f}".center(50))
    print(f"Capital con interés compuesto: ${interes_Compuest:,.0f}".center(50))
    print("\n")
    

if __name__ == "__main__":
    investor, interes, number_Ages = user_Dates()
    interes_Simple, interes_Compuest = obtain_Capital (investor, interes, number_Ages)
    print_Capital(investor, interes, number_Ages, interes_Simple, interes_Compuest)