import os
from re import I
os.system("cls")

"""

12.	Cierta empresa proporciona un bono mensual a sus trabajadores,
el cual puede ser por su antigüedad o bien por el monto de su sueldo (el que sea mayor),
de la siguiente forma:

Cuando la antigüedad es mayor a 2 años pero menor a 5, se otorga 20 % de su sueldo;
cuando es de 5 años o más, 30 %.

Ahora bien, el bono por concepto de sueldo,

si éste es menor a $1000, se da 25 % de éste, cuando éste es mayor a $1000, pero menor o igual a $3500,
se otorga 15% de su sueldo, para más de $3500. 10%.

Realice un programa en Python correspondiente para
calcular los dos tipos de bono, asignando el mayor.

"""

antiguedad=int(input("Digite la antiguedad del trabajador en años:  "))
salario=float(input("Digite el salario del trabajador:  "))
salario1=float()
salario2=float()

if antiguedad>=2 and antiguedad<5:
    salario1+=salario+(salario*20)/100
elif antiguedad>=5:
    salario1+=salario+(salario*30)/100

if salario<1000:
    salario2+=salario+(salario*25)/100
elif salario>=1000 and salario<=3500:
    salario2+=salario+(salario*15)/100
elif salario>3500:
    salario2+=salario+(salario*10)/100

if salario1>salario2:
    print("Se calcula un mayor beneficio por antiguedad para un salario total de: $",salario1)
else:
    print("Se calcula un mayor beneficio por salario para un salario total de: $",salario2)