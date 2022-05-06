"""

    8.	Realizar un sistema utilizando el lenguaje python que solicite dos numeros por teclado y permita elegir entre 3 opciones en un menú que son:
        a.	Mostrar La suma de dos numero
        b.	Mostrar la resta de dos numesios
        c.	Mostrar la multiplicación de 2 numero

"""

num1=float(input("Digite el 1er numero:   "))
num2=float(input("Digite el 2do numero:   "))
opcion=int(input("""Digite [1] para suma
Digite [2] para resta
Digite [3] para multiplicar
"""))

if opcion==1:
    print("La suma de sus numeros es",num1+num2)
elif opcion==2:
    print("La resta de sus numeros es",num1-num2)
elif opcion==3:
    print("El producto de sus numeros es",num1*num2)
else:
    print("Opcion Invalida")