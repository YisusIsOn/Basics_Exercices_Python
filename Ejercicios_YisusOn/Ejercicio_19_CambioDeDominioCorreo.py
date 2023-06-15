"Ejercicio 19"

"""
Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico 
con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.
"""
"Modo Basico"

print("\n")
print("".center(50, "-"))

user_Email = input("Ingrese su correo electronico: ")
email_Change = "ceu.es"
email_Vector = []
email_SplitName = user_Email.split("@")[0]
email_SplitDomain = user_Email.split("@")[1]

print("El nuevo correo es: " + email_SplitName + "@" +email_SplitDomain.replace(email_SplitDomain, "ceu.es"))