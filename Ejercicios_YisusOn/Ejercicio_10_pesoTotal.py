"Ejercicio 10"
"Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística"
"les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda."
"Cada payaso pesa 112 g y cada muñeca 75 g."
"Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado."

def datos_Ingresados():
    print("\n")
    num_Payasos= int(input("Ingrese el numero de payasos a comprar: "))
    num_Muñecas= int(input("Ingrese el numero de muñecas a comprar: "))
    return num_Payasos, num_Muñecas 

def calculo_Peso(num_Payasos, num_Muñecas):
    res_Payasos = (112 * num_Payasos)
    res_Muñeca = (75 * num_Muñecas)
    sum_Total = res_Muñeca + res_Payasos
    return sum_Total

def print_Resultado(num_Payasos, num_Muñecas, sum_Total):
    print("\n")
    print(f"Con los {num_Payasos:.0f} payasos y {num_Muñecas:.0f} muñecas tienes un peso total de {sum_Total:.0f}g")
    print("\n")

if __name__ =="__main__":
    num_Payasos, num_Muñecas = datos_Ingresados()
    sum_Total = calculo_Peso(num_Payasos, num_Muñecas)
    print_Resultado(num_Payasos, num_Muñecas, sum_Total)