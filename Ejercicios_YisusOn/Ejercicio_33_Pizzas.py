"Ejercicio 33"

"""
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, 
y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. 
Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. 
Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
"""


def ingresoDatos():

    print("\n")
    print("".center(100,"-"))
    print("BELLA NAPOLI".center(100))
    print("".center(100,"-"))

    veg = input("Quiere una pizza vegetariana: ")
    print("".center(100,"-"))

    return veg

def condicionalpizza(veg):

    if veg.lower() == "si":
        print("Escoja un ingrediente para su pizza vegetariana: ".center(100))
        print("".center(100,"-"))
        print("Ingredientes".center(100) + "\n" + "• Pimiento".center(100) + "\n" + "• Tofu".center(100))
        print("".center(100,"-"))
        ingrediente = input("INGREDIENTE: ")
        print("".center(100,"-"))

        if ingrediente.lower() == "tofu" or ingrediente.lower() == "pimiento":
            return ingrediente
        else:
            print("Ingresó un ingrediente inválido" + "\n")
            return None

    elif veg.lower() == "no":

        print("Escoja un ingrediente para su pizza no vegetariana: ")
        print("".center(100,"-"))
        print("Ingredientes".center(100) + "\n" + "• Peperoni".center(100) + "\n" + "• Jamon".center(100) + "\n" + "• Salmón".center(100))
        print("".center(100,"-"))
        ingrediente = input("INGREDIENTE: ")
        print("".center(100,"-"))
        
        if ingrediente.lower() == "peperoni" or ingrediente.lower() == "jamon" or ingrediente.lower() == "salmon":
            return ingrediente
        else:
            print("Ingresó un ingrediente inválido" + "\n")
            return None

    else:
        print("Ingrese una entrada valida SI o NO")
        return None

def salidaDatos(veg, ingrediente):
    
    if veg.lower() == "si":

        if ingrediente.lower() == "pimiento":
            print("La pizza es vegetariana y cuenta con los siguientes ingredientes: ")
            print("{:^100}".format("• Mozzarella") + "\n" + "{:^95}".format("• Queso") + "\n" + "{:^98}".format("• Pimiento") + "\n")

        elif ingrediente.lower() == "tofu":
            print("La pizza es vegetariana y cuenta con los siguientes ingredientes: ")
            print("{:^100}".format("• Mozzarella") + "\n" + "{:^95}".format("• Queso") + "\n" + "{:^94}".format("• Tofu") + "\n")

    elif veg.lower() == "no":
        if ingrediente.lower() == "peperoni":
            print("La pizza no es vegetariana y cuenta con los siguientes ingredientes: ")
            print("{:^100}".format("• Mozzarella") + "\n" + "{:^95}".format("• Queso") + "\n" + "{:^98}".format("• Peperoni") + "\n")

        elif ingrediente.lower() == "jamon":
            print("La pizza es vegetariana y cuenta con los siguientes ingredientes: ")
            print("{:^100}".format("• Mozzarella") + "\n" + "{:^95}".format("• Queso") + "\n" + "{:^95}".format("• Jamon") + "\n")
        
        elif ingrediente.lower() == "salmon":
            print("La pizza es vegetariana y cuenta con los siguientes ingredientes: ")
            print("{:^100}".format("• Mozzarella") + "\n" + "{:^95}".format("• Queso") + "\n" + "{:^97}".format("• Salmón") + "\n")

if __name__ == "__main__":
    veg = ingresoDatos()
    ingrediente = condicionalpizza(veg)
    if ingrediente is not None:
        salidaDatos(veg, ingrediente)
