"""
    5.	Crear una aplicación usando python que resuelva el siguiente problema,
    la jornada de trabajo es de 48 horas, se debe de solicitar las horas
    trabajadas y el pago por hora, si las horas sobrepasan la jornada semanal,
    deben de pagar las horas extras el doble.

"""

horastrabajo=int(input("Digite las horas trabajadas:    "))
salariohora=int(input("Digite su salario por hora:  "))
salariototal=horastrabajo*salariohora
extras=horastrabajo-48

if horastrabajo<=48:
    print("Su salario es de:",salariototal,"(No hizo horas extra)")
elif horastrabajo>48:
    print("Su salario es de:",(extras*salariohora)+salariototal),"con un total de:",extras,"horas extra"