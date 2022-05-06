import os
os.system("cls")

"""

8.	“El oso hambriento” ofrece hamburguesas sencillas, dobles y triples, las cuales tiene un
costo de $20.00, $25.00 y $28.00 respectivamente. La empresa acepta tarjetas de crédito con
un cargo de 5 % sobre la compra. Suponiendo que los clientes adquieren sólo un tipo de hamburguesa,
realice un programa para determinar cuánto debe pagar una persona por N hamburguesas.

"""

sencillas=int(input("Cuantas Hamburguesas Sencillas:    "))
dobles=int(input("Cuantas Hamburguesas Dobles:  "))
triples=int(input("Cuantas Hamburguesas Triples:    "))

metodo=input("Desea Pagar Con Tarjeta [Si o No]?:   ")

precio_sencillas=sencillas*20
precio_dobles=dobles*25
precio_triples=triples*28

total=precio_sencillas+precio_dobles+precio_triples
tarjeta=(total*5)/100

if metodo=="si" or metodo=="Si" or metodo=="sI" or metodo=="SI":
    print("Total a pagar por",sencillas,"Sencillas,",dobles,"Dobles y",triples,"Triples:    $",total+tarjeta)
else:
    print("Total a pagar por",sencillas,"Sencillas,",dobles,"Dobles y",triples,"Triples:    $",total)