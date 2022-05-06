"""4. Realizar un programa en python que lea por teclado las 5 notas obtenidas por un
usuario (comprendidas entre 1 y 100). A continuación, debe mostrar todas las notas,
y el promedio de las notas ingresadas."""
import os
os.system("cls")

notas=[]
contador=1
sumatoria=0

for i in range(5):
    print("Digite la Nota #",contador)
    ingreso=int(input())
    if ingreso>0 and ingreso<=100:
        notas.append(ingreso)
        contador=contador+1
    else:
        print("Nota no valida, solo numeros entre 1 y 100")

for i in notas:
    sumatoria=sumatoria+i

promedio=sumatoria/5
contador=1

print("---------Resultados---------")

for i in notas:
    print("Nota #",contador,"=",i)
    contador=contador+1

print("Promedio:",promedio)