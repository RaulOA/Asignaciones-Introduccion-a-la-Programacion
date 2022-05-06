"""

    10.	Crear un programa que permita al usuario elegir un candidato por el cual votar.
    Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verde,
    candidato C por el partido azul. Según el candidato elegido (A, B ó C) se le debe imprimir el mensaje
    “Usted ha votado por el partido [color que corresponda al candidato elegido]”.
    Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles,
    indicar “Opción errónea”. Pista: Si la letra ingresada por el usuario es en minúscula,
    el programa debe convertirla en mayúscula.

"""

eleccion=input("""Elija su candidato:
A) Partido Rojo
B) Partido Verde
C) Partido Azul
:       """)

eleccion=eleccion.upper()

if eleccion=="A":
    print("Usted ha votado por el Partido Rojo")
elif eleccion=="B":
    print("Usted ha votado por el Partido Verde")
elif  eleccion=="C":
    print("Usted ha votado por el Partido Azul")
else:
    print("Opcion Erronea")