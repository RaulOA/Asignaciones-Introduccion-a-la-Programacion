Algoritmo sin_titulo
	modulo <- 0
	Repetir
		Escribir 'Ingrese un numero del 1 al 5'
		Leer num
		Si num>=1 Y num<=5 Entonces
			modulo <- num MOD 2
		SiNo
			Escribir 'Dato no Valido'
		FinSi
	Hasta Que num>=1 Y num<=5
	Si modulo=0 Entonces
		Escribir 'El numero [',num,'] es Par'
	SiNo
		Escribir 'El numero [',num,'] es Impar'
	FinSi
FinAlgoritmo
