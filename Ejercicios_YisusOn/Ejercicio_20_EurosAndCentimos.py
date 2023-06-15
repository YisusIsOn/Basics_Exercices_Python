"Ejercicio 20"

"""
Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales 
y muestre por pantalla el número de euros y el número de céntimos del precio introducido.
"""
"Modo Basico"

print("\n")
print("".center(70, "-"))
print("DATO DE FACTURA".center(70))
print("".center(70, "-"))

product_Price = input("Ingrese el precio el producto en euros (€) con dos decimales: ")

product_Vector = []
product_SplitCentimo = ""
product_SplitEuro = ""

if "," in product_Price:
    product_SplitEuro = product_Price.split(",")[0]
    product_SplitCentimo = product_Price.split(",")[1]

elif "." in product_Price:
    product_SplitEuro = product_Price.split(".")[0]
    product_SplitCentimo = product_Price.split(".")[1]

else:
    print("Entrada inválida. El precio debe contener dos decimales separados por '.' o ','.")
    exit()

print("".center(70, "-"))
print("FACTURA".center(70))
print("".center(70, "-"))
print("Los euros son:    " + product_SplitEuro)
print("Los centimos son: " + product_SplitCentimo)
print(product_SplitEuro + " euros y " + product_SplitCentimo + " centimos." + "\n")
