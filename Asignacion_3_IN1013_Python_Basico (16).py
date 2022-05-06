import os
from unittest.case import _AssertRaisesContext
os.system("cls")

"""

16.	Crea un programa en Python que imprima una pirámide de asteriscos. Nosotros le pasamos la altura de la pirámide por teclado

"""

num=int(input("Ingrese el tamaño de la escalera: "))
espacios=num
multiplo=1

for i in range(num):

    print(" "*espacios,"*"*multiplo)
    espacios=espacios-1
    multiplo+=2