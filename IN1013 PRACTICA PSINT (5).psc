Algoritmo Ejercicio_5
	//Crear el diagrama de flujo para un programa que pida un número entero 
	// distinto de cero y nos muestre en pantalla un mensaje indicándonos si 
	// el número es par o impar.
	resultado<-0
	Repetir
		Escribir "Digite un numero distinto a cero:"
		Leer num
	si num == 0
		Entonces
		Escribir "Su numero no es valido, porfavor digite nuevamente..."
	SiNo resultado<-num%2
		FinSi
	Hasta Que num>0
	si resultado==1
		Entonces
		Escribir "El numero [",num,"] es IMPAR"
	SiNo
		Escribir "El numero [",num,"] es PAR"
	FinSi
		Escribir "Escrito por: Sebastian Naranjo, David Porras y Raul Ortega"
	
FinAlgoritmo
