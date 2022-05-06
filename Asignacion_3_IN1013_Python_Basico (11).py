import os
from re import I
os.system("cls")

"""

11.	Realizar un programa en Python que le pregunte al usuario las notas de los estudiantes de una en una,
el mismo programa le debe preguntar si desea ingresar continuar o no,
no debe de importar las mayúsculas o minúsculas,
al final debe de sacar el promedio de todas las notas ingresadas.

"""

salir="s"

while salir=="si" or salir=="Si" or salir=="sI" or salir=="SI" or salir=="s" or salir=="S":

    print("Digite las siguientes notas en la escala de 0 a 100")

    parcial1=float(input("Digite la nota del 1er Parcial:  "))
    parcial1=(parcial1*10)/100

    parcial2=float(input("Digite la nota del 2do Parcial:  "))
    parcial2=(parcial2*20)/100

    parcial_3=float(input("Digite la nota del 3er Parcial:  "))
    parcial_3=(parcial_3*20)/100

    proyecto_1=float(input("Digite la nota del 1er Proyecto:  "))
    proyecto_1=(proyecto_1*5)/100

    proyecto_2=float(input("Digite la nota del 2do Proyecto:  "))
    proyecto_2=(proyecto_2*15)/100

    practicas=float(input("Digite la nota de las Practicas:  "))
    practicas=(practicas*15)/100

    asignaciones=float(input("Digite la nota de las Asignaciones:  "))
    asignaciones=(asignaciones*15)/100

    promedio=parcial1+parcial2+parcial_3+proyecto_1+proyecto_2+practicas+asignaciones
    promedio=round(promedio,2)

    print("El promedio del estudiante es de",promedio)

    salir=input("Continuar? S o N:  ")

print("Adios")