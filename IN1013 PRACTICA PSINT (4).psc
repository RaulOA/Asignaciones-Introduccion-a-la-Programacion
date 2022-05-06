Algoritmo Ejercicio_4
	// Desarrolle un algoritmo que permita leer tres valores y almacenarlos en las 
	// variables A, B y C respectivamente. El algoritmo debe imprimir cual es el mayor.
	Escribir "Digite el 1er digito"
	Leer variable_a
	Escribir "Digite el 2da digito"
	Leer variable_b
	Escribir "Digite el 3er digito"
	Leer variable_c
			si variable_a>variable_b&variable_a>variable_c 
		Entonces
		Escribir "El 1er digito que corresponde a:[",variable_a,"] es el mayor"
			SiNo 
				si variable_b>variable_a&variable_b>variable_c
					Entonces
					Escribir "El 2do digito que corresponde a:[",variable_b,"] es el mayor"
				SiNo
					si variable_c>variable_a&variable_c>variable_b
						Entonces
						Escribir "El 3er digito que corresponde a:[",variable_c,"] es el mayor"
					SiNo
						Escribir "Existen datos de igual valor"
					FinSi					
				FinSi		
	FinSi
	Escribir "Escrito por: Sebastian Naranjo, David Porras y Raul Ortega"
FinAlgoritmo
