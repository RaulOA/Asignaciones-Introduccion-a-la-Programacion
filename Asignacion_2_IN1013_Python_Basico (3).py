"""

    3.	Crear un programa utilizando Python que permita determinar el salario
    a pagar a un empleado teniendo como entradas el salario diario y el número
    de días trabajados. Tenga en cuenta que al empleado se le debe descontar
    el 10% por concepto de pensión y 15% por concepto de salud.

"""

from http.client import NETWORK_AUTHENTICATION_REQUIRED


salario=float(input("Digite su salario diario:   "))
diastrabajo=int(input("Digite los dias trabajados:   "))
pension=float((((salario*diastrabajo)*10)/100))
salud=float((((salario*diastrabajo)*15)/100))
salarioneto=(salario*diastrabajo)-pension-salud

print("Su salario neto es de: ",salarioneto,"por un total de",diastrabajo,"dias trabajados")