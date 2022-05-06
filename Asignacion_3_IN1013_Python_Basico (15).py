import os
os.system("cls")

"""

15.	Crea un programa en Python que imprima una escalera de números,
siendo cada linea números empezando en uno y acabando en el numero de la linea.

"""

num=int(input("Ingrese el tamaño de la escalera: "))
escalera="1"
contador=2
contadorstr=str(contador)

for i in range(num):
    print(escalera)
    escalera=escalera+contadorstr
    contador=contador+1
    contadorstr=str(contador)