"""

    15.	Para tributar un determinado impuesto se debe ser mayor de 16 años
    y tener unos ingresos iguales o superiores a 1000 € mensuales.
    Escribir un programa que pregunte al usuario su edad y sus ingresos
    mensuales y muestre por pantalla si el usuario tiene que tributar o no.

"""

edad=int(input("Cual es su edad:    "))
ingreso=int(input("Cuales es su ingreso mensual:    "))

if edad>16 and ingreso>1000:
    print("Debe de tributar")
else:
    print("No debe de tributar aun")