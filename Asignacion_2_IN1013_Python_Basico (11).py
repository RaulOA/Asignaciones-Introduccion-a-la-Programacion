"""

    11.	Crear un programa que pida al usuario una letra, y si es vocal,
    muestre el mensaje "Es vocal". Sino, decirle al usuario que no es vocal.

"""

vocales="a","e","i","o","u"
letra=input("Digite una letra:  ")
letra=letra.lower()

if letra in vocales:
    print("Su letra es una vocal")
else:
    print("Su letra es una consonante")