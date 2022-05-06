import os
from re import I
os.system("cls")

"""

13.	Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó $10,
el segundo $20, el tercero $40 y así sucesivamente. Realice un programa en Python para
determinar cuánto debe pagar mensualmente y el total de lo que pagó después de los 20 meses

"""

mes=1
cantidad1=10
cantidad2=10

for i in range(20):
    print("El mes",mes,"pagó $",cantidad1)
    mes+=1
    cantidad1=cantidad1*2
    if mes==21:
        break
    cantidad2=cantidad1+cantidad2

print("La suma de las 20 cuotas es de:",cantidad2)