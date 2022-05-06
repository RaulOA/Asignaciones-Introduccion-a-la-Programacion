"""1. Realizar un programa en python que inicialice una lista con 10 valores aleatorios (del
1 al 10, para esto debe de usar la librería random) y posteriormente muestre en
pantalla cada elemento de la lista junto con su cuadrado y su cubo."""
import os
os.system("cls")
import random

numeros=[]

for a in range(10):
    numeros.append(random.randint(1,10))

print (numeros)

for b in numeros:
    print("Numero=",b,", Su Cuadrado=",b**2,", Su Cubo=",b**3)