"""6. Realizar un programa en Python que le pregunte al usuario las notas de los
estudiantes de una en una, el mismo programa le debe preguntar si desea ingresar
continuar o no, no debe de importar las mayúsculas o minúsculas, al final debe de
sacar el promedio de todas las notas ingresadas."""
import os
os.system("cls")
resultados=[]
sumatoria=0

materia=input("Digita el nombre de la materia: ")
materia=materia.upper()
nota=int(input("Digite la nota: "))
resultados.append([materia,nota])
continuar=input("Desea continuar? S/N: ")
continuar=continuar.lower()

while continuar=="s" or continuar=="si":
    materia=input("Digita el nombre de la materia: ")
    materia=materia.upper()
    nota=int(input("Digite la nota: "))
    resultados.append([materia,nota])
    continuar=input("Desea continuar? S/N : ")
    continuar=continuar.lower()

for a,b in resultados:
    sumatoria=sumatoria+b

sumatoria=sumatoria/len(resultados)

for a,b in resultados:
    print(a,":",b)

print("Usted tiene un promedio de:",sumatoria)