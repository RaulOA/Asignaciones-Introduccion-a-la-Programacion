"""7. Realizar un programa en Python que declare tres listas ‘lista_1’, ‘lista_2’ y ‘lista_3’ de cinco
enteros cada uno, pida valores para ‘lista_1’ y ‘lista_2’ y calcule lista_3=lista_1+lista_2."""
from operator import contains
import os
os.system("cls")

lista1=[]
lista2=[]
lista3=[]
contador=1

for i in range(5):
    print("Entero #",contador,"para la lista 1")
    entero1=input()
    digito1=entero1.isdigit()
    print("Entero #",contador,"para la lista 2")
    entero2=input()
    digito2=entero2.isdigit()
    if digito1==True and digito2==True:
        entero1=int(entero1)
        lista1.append(entero1)
        entero2=int(entero2)
        lista2.append(entero2)
        contador=contador+1
    else:
        print("Ingreso Incorrecto, solo numeros enteros")

lista3.append([lista1,lista2])
print(lista3)