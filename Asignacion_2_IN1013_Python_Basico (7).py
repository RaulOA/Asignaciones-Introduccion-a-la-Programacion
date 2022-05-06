"""
    7.	Realizar un sistema utilizando el lenguaje python que solicite 2 numeros por teclado y determine los siguientes aspectos:
        a.	Si los dos numeros son iguales
        b.	Si los dos numeros son diferentes
        c.	Si el primero es mayor que el segundo
        d.	Si el segundo es mayor o igual que el primero
        e.	Si son numeros o letras

"""

texto1=input("Digite un numero: ")
texto2=input("Digite otro numero:   ")

if texto1==texto2:
    print("Los dos numeros son inguales")
elif texto1!=texto2:
    print("Sus numeros son diferentes")
    if texto1>texto2:
        print("Y el primer numero es el mayor")
    elif texto1<texto2:
        print("Y el segundo numero es el mayor")

if(texto1 >= '0' and texto1 <= '9'):
    print(texto1," Esto es un numero")
else:
    print(texto1,"  Esto no es un numero")

if(texto2 >= '0' and texto2 <= '9'):
    print(texto2," Esto es un numero")
else:
    print(texto2,"  Esto no es un numero")