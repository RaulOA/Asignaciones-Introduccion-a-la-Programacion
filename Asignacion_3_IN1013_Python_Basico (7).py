import os
os.system("cls")

"""

7.	El director de una escuela está organizando un viaje de estudios, y requiere determinar cuánto
debe cobrar a cada alumno y cuánto debe pagar a la compañía de viajes por el servicio. La forma de
cobrar es la siguiente: si son 100 alumnos o más, el costo por cada alumno es de $65.00; de 50 a 99 alumnos,
el costo es de $70.00, de 30 a 49, de $95.00, y si son menos de 30, el costo de la renta del autobús es de $4000.00,
sin importar el número de alumnos.

"""

cantidad=int(input("Cuantos alumnos son?:   "))

if cantidad>=100:
    print("Debes cobrar $65 por alumno y un total de $",cantidad*65,"a la compañia de viajes")
elif cantidad>=50 and cantidad<=99:
    print("Debes cobrar $70 por alumno y un total de $",cantidad*70,"a la compañia de viajes")
elif cantidad>=30 and cantidad<=49:
    print("Debes cobrar $95 por alumno y un total de $",cantidad*95,"a la compañia de viajes")
elif cantidad<30:
    print("Debes cobrar $",4000//cantidad," por alumno y un total de $ 4000 a la compañia de viajes")