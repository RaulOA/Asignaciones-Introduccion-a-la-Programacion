import os
os.system("cls")

"""

10.	Un profesor tiene un salario inicial de $1500, y recibe un incremento de 10 % anual durante 6 años.
¿Cuál es su salario al cabo de 6 años? ¿Qué salario ha recibido en cada uno de los 6 años?

"""

salario=1500
contador=2
print("""Salario Inicia
$ 1500""")
for i in range(5):
    print("Salario del año",contador)
    contador+=1
    salario+=(salario*10)/100
    salario=round(salario,2)
    print("$",salario)