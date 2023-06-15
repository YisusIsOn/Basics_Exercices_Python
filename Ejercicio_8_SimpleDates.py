"Ejercicio 8"
"Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c>"
"y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente."

def entrada():
    numero_n=int(input("Por favor ingrese el primer entero: "))
    numero_m=int(input("Por favor ingrese el segundo entero: "))
    return numero_n, numero_m

def calculos(numero_n,numero_m):
    cociente_Sol=float(numero_n/numero_m)
    resto_Sol=float(numero_n % numero_m)
    return cociente_Sol, resto_Sol

def print_Resuilts (cociente_Sol, resto_Sol):
    print("El cociente de los numeros es: "+ str(cociente_Sol))
    print("La resta de los numeros es: "+ str(resto_Sol))
    print(str(numero_n) + " entre " + str(numero_m) + " da un cociente de " + str(cociente_Sol) + " y un resto de " + str(resto_Sol))

if __name__ == "__main__":
    numero_n, numero_m = entrada()
    cociente_Sol, resto_Sol = calculos(numero_n, numero_m)
    print_Resuilts(cociente_Sol, resto_Sol)