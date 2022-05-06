"""

    6.	Utilizando operadores lógicos determine si una cadena de texto
    introducida por el usuario tiene una logitud mayor o igual a 3 o menor
    igual a 12, se debe de mostrar True o false.

"""

texto=input("introduzca una cadena de texto:    ")
lon=len(texto)

if lon>=3 and lon<=12:
    print(True)
else:
    print(False)