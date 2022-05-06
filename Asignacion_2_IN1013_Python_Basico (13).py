"""
    13.	Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo.
    El programa debe determinar que tipo de triangulo es, teniendo en cuenta los siguiente:
        Si se cumple Pitágoras entonces es triángulo rectángulo
        Si sólo dos lados del triángulo son iguales entonces es isósceles.
        Si los 3 lados son iguales entonces es equilátero.
        Si no se cumple ninguna de las condiciones anteriores, es escaleno.

"""

ladoa=int(input("Digite la medida del lado A del triangulo: "))
ladob=int(input("Digite la medida del lado B del triangulo: "))
ladoc=int(input("Digite la medida del lado C o hipotenusa del triangulo: "))

x=(ladoa**2)+(ladob**2)
y=ladoc**2

if x == y:
    print("Es un triangulo rectangulo")
elif ladoa==ladob==ladoc:
    print("Es un triangulo Equilatero")
elif ladoa == ladob or ladoa == ladoc or ladob == ladoc:
    print("Es un triangulo Isosceles")
elif ladoa!=ladob!=ladoc:
    print("Es un triangulo Escaleno")