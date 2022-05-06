Algoritmo Ejercicio_3
	//	Desarrolle un algoritmo que realice la sumatoria de los números 
	// enteros comprendidos entre el 1 y el 10,es decir, 1 + 2 + 3 + .... + 10.
	val1 <- 1
	val2 <- 2
	aux <- 0
	aux <- val1+val2
	Escribir "1+2= [",aux,"]"
	val2 <- val2+1
	Repetir
		Escribir aux,"+",val2,"= [",aux+val2,"]"
		aux <- val2+aux
		val2 <- val2+1
	Hasta Que aux==55
	Escribir 'La suma total del 1 al 10 corresponde a: [',aux,']'
	Escribir "Escrito por: Sebastian Naranjo, David Porras y Raul Ortega"
FinAlgoritmo
