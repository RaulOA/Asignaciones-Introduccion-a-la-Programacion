"""5. Realizar un programa en python que declare una lista y la vaya llenando de números
hasta que introduzcamos un número negativo. Entonces se debe imprimir en pantalla
los números introducidos."""
import os
os.system("cls")

lista=[]

while True:
    print("introduzca un Numero, un negativo cierra el programa")
    numero=int(input())
    lista.append(numero)
    if numero<0:
        break
print(lista)
