Algoritmo practica_5_examen
	//Diseñar un diagrama de flujo que lea un número, validar que sea mayor que 0 
	//e indicar la cantidad de números enteros que hay entre uno y el valor leído.
	contador<-0
	Repetir
		Escribir "Digite un numero positivo diferente de 0"
		Leer num
		Si num>0 Entonces
			Repetir
				contador<-contador+1
			Hasta Que contador==num-1
			Escribir "Entre ",num," y el 1 hay ",contador," numeros enteros"
		SiNo
			Escribir "Ni el 0 ni los numeros negativos son validos"
		Fin Si
	Hasta Que num>0
FinAlgoritmo
