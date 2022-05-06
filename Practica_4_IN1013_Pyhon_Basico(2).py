"""2. Escribir un programa que almacene en una lista los siguientes
precios,100,50,65,98,65,45,12,1,6,5,4444,30, y muestre por pantalla el menor y el
mayor de los precios."""
import os
os.system("cls")

lista=[100,50,65,98,65,45,12,1,6,5,4444,30,]
mayor=0
menor=lista[0]

for i in lista:
    if i>mayor:
        mayor=i
    if i<menor:
        menor=i

print("Mayor:",mayor,"Menor:",menor)