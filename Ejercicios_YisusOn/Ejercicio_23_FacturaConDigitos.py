"Ejercicio 23"

"""
Escribir un programa que pregunte el nombre de un producto, su precio y un número de unidades 
y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales,
 el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.
"""

def entrada_Datos():
    print("\n")
    print("PRODUCTOS".center(100))
    print("".center(100, "-"))
    numero_Producto = int(input("Ingrese la cantidad de productos a comprar: "))

    vector_Productos = []
    vector_Precio = []
    vector_Unidades = []

    for i in range(numero_Producto):
        producto = input("Ingrese el producto " + str(i+1) + ": ")
        vector_Productos.append(producto)
        precio = float(input("Ingrese el precio    : "))
        vector_Precio.append(precio)
        unidades = int(input("Ingrese las unidades : "))
        vector_Unidades.append(unidades)
        print("".center(50, "-"))

    return vector_Productos, vector_Precio, vector_Unidades, numero_Producto


def salida_Datos(vector_Productos, vector_Precio, vector_Unidades):
    print("".center(100, "-"))
    print("FACTURA".center(100))
    print("".center(100, "-"))

    total_Compra = 0

    for i in range(len(vector_Productos)):
        producto = vector_Productos[i]
        precio = vector_Precio[i]
        unidades = vector_Unidades[i]
        subtotal = precio * unidades
        total_Compra += subtotal
        print(f"• El {producto} tiene un precio de {precio:.2f} con {unidades:0>3.0f} unidades tiene un precio de {subtotal:.2f}" + "\n")

    print(f"El coste total de la compra es: {total_Compra:0>11,.2f}".center(100) + "\n")
    print("".center(100, "-"))

if __name__ == "__main__":
    vector_Productos, vector_Precio, vector_Unidades, numero_Producto = entrada_Datos()
    salida_Datos(vector_Productos, vector_Precio, vector_Unidades)
