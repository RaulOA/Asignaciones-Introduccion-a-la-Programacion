import os
os.system("cls")

"""

9.	El consultorio del Dr. Mata Sanos tiene como política cobrar la consulta con base en el número de cita, de la siguiente forma:
• Las tres primeras citas a $200.00 c/u.
• Las siguientes dos citas a $150.00 c/u.
• Las tres siguientes citas a $100.00 c/u.
• Las restantes a $50.00 c/u, mientras dure el tratamiento.
Se requiere un algoritmo para determinar:
a) Cuánto pagará el paciente por la cita.
b) El monto de lo que ha pagado el paciente por el tratamiento

"""

consulta=int(input("Numero de Cita?:  "))
tratamiento=int(input("Valor del Tratamiento?:  "))

if consulta<=3:
    print("""Precio por consulta: $200
    Precio por tratamiento: $""",tratamiento)
elif consulta>3 and consulta<=5:
    print("""Precio por consulta: $150
    Precio por tratamiento: $""",tratamiento)
elif consulta>5 and consulta<=8:
    print("""Precio por consulta: $100
    Precio por tratamiento: $""",tratamiento)
else:
    print("""Precio por consulta: $50
    Precio por tratamiento: $""",tratamiento)