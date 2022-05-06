"""

    4.	Crear un programa utilizando Python que permita calcular el valor final a
    pagar en una súper tienda en donde se aplican los siguientes descuentos:
        a) Por compras entre 10000 y 20000 el 10%
        b) Por compras entre 20001y 50000 el 30%
        c) Por compras superiores a 50000 el 50%


"""

montobruto=int(input("Digite el monto total de la compra:    "))

if montobruto<10000:
    print("No se aplica descuento")
elif montobruto>=10000 and montobruto<=20000:
    print("Aplica un descuento de: ",montobruto,"-",(montobruto*10)/100)
elif montobruto>20000 and montobruto<=50000:
    print("Aplica un descuento de: ",montobruto,"-",(montobruto*30)/100)
elif montobruto>50000:
    print("Aplica un descuento de: ",montobruto,"-",(montobruto*50)/100)