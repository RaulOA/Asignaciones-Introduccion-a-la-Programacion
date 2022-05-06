import os
os.system("cls")

"""

3.	Realizar un programa en Python que le permita al usuario ingresar dos años y
luego imprima todos los años en ese rango, desde luego el primer año digitado tiene que
ser menor al segundo si no el programa no debe de funcionar.

"""

year1=int(input("Digite el año de inicio:   "))
year2=int(input("Digite el año final:   "))

for i in range(year1,year2+1):
    print(i)