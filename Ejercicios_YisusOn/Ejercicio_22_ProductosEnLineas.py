"Ejercicio 22"

"""
Escribir un programa que pregunte por consola por los productos de una cesta de la compra, 
separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.
"""

def ingreso_Productos():
    print("\n")
    print("".center(70,"-"))
    productos = input("Ingrese los productos de la cesta de compra y separelos por coma(,): "+"\n")
    print("".center(70,"-"))
    return productos

def arreglo_Producto(productos):
    sinEspacio_Productos = productos.replace(" ","")
    split_productos = sinEspacio_Productos.split(",")
    return split_productos

def salida(split_productos):

    print("LA LISTA DE COMPRA ES:".center(70))
    print("".center(70,"-"))

    for producto in split_productos:
        print("{:^0}".format("• " + producto.title())) 

    print("".center(70,"-"))

if __name__ == "__main__":
    productos = ingreso_Productos()
    split_productos = arreglo_Producto(productos)
    salida(split_productos)
