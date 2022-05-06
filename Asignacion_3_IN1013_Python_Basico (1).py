import os
os.system("cls")

"""

1.	Realizar un programa en Python que le pregunte al usuario cuántos números se van a
introducir por teclado por ejemplo 10 numeros, pida esos números y escriba cuántos
negativos ha introducido y cuantos positivos.

"""

espacios=int(input("Cuantos numeros desea introducir?:   "))
positive=0
negative=0

for i in range(espacios):
    num=int(input("Numero: "))
    if num < 0:
        negative+=1
    else:
        positive+=1

print("Usted ha digitado",positive,"numeros positivos y",negative,"numeros negativos")