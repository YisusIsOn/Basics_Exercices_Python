"Ejercicio 12"

"""
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. 
Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.
"""

def barras_Novendidads():
    print("\n")
    print("LA PANADERIA".center(50))
    print("".center(50,"-"))
    br_Nv = int(input("Ingrese el numero de barras vendidas que no son del dia: "))
    return br_Nv

def calculo_Pan(br_Nv):
    unPan = 3.49
    descuento = 0.6
    panViejo = unPan * descuento
    precioPanViejo = panViejo * br_Nv
    precioFinal = br_Nv * unPan * (1 - descuento)
    return unPan, precioPanViejo, precioFinal

def print_Totalpan (unPan, precioPanViejo, br_Nv, precioFinal):
    print("\n")
    print("FACTURA".center(50))
    print("".center(50,"-"))
    print("El valor habitual de una barra de pan es: "+ str(unPan) + "€")
    print("El Descuento del pan por no ser fresco es del 60%")
    print(f"El valor de las {br_Nv:.0f} barras de pan no frescas es: {precioPanViejo:.3f}€")
    print(f"El coste final a pagar es: {precioFinal:.3f}€")
    print("\n")

if __name__=="__main__":
    br_Nv = barras_Novendidads()
    unPan, precioPanViejo, precioFinal = calculo_Pan(br_Nv)
    print_Totalpan (unPan, precioPanViejo, br_Nv, precioFinal)