Algoritmo Practica_1_del_examen
	//Diseñar un Algoritmo en diagrama de flujo que lea dos números, 
	//solicitar al usuario si los quiere sumar o multiplicar y realizar la acción elegida por usuario.
	Escribir "Digite el 1er numero"
	Leer num1
	Escribir "Digite el 2do numero"
	Leer num2
	Repetir
		Escribir "^[1] para Multiplicar o [2] para Sumar"
		Leer operacion
		Si operacion==1 Entonces
			mult<-num1*num2
			Escribir num1,"x",num2,"= ",mult
		SiNo
			Si operacion==2 Entonces
				suma<-num1+num2
				Escribir num1,"+",num2,"= ",suma
			SiNo
				Escribir "Operasion Invalida, Digite 1 o 2"
			Fin Si
		Fin Si
	Hasta Que operacion==1 o operacion==2
FinAlgoritmo
