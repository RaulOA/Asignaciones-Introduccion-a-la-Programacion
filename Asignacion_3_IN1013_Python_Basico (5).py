import os
os.system("cls")

"""

5.	Escribir un programa que pregunte al usuario una cantidad a invertir,
el interés anual y el número de años que desea invertir, y muestre por
pantalla el capital obtenido en la inversión cada año que dura la inversión.

"""

cantidad=int(input("Cuanto quiere invertir?:    "))
interes=int(input("Cual es el porcentaje de interes anual?:    "))
years=int(input("Por cuantos años desea invertir?:    "))
capital=((cantidad*interes)/100)*years
print("El monto obtenido al final de",years,"años sera de:    ",capital)