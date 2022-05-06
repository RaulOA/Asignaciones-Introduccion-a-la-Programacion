import os
os.system("cls")

"""

4.	En una empresa trabajan n cantidad de  empleados cuyos sueldos oscilan
entre 1000 dólares y 2000 dólares. Realizar un programa que informe de
cuantos empleados cobran menos de 1500 dolares y cuantos más de 1500 dolares.
Informar también del total que gasta la empresa en pagar a sus empleados.

"""

empleados=int(input("Cuantos empleados tiene?:   "))
positive=0
negative=0
suma=0
contador=1

for i in range(empleados):
    print("Salario del empleado #",contador)
    num=int(input())
    contador+=1
    suma+=num

    if num <= 1500:
        negative+=1
    else:
        positive+=1

print("""Usted tiene",positive,"empleados que ganan mas de $1500 y",negative,"que cobran menos de eso, ademas su empresa gasta un total de $",suma,"en salarios""")