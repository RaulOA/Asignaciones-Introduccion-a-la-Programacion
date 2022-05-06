Algoritmo sin_titulo
	Escribir 'digite el primer dato'
	Leer dato1
	Escribir 'digite el segundo dato'
	Leer dato2
	Escribir 'digite el tercer dato'
	Leer dato3
	Si dato1>dato2 Y dato2>dato3 Entonces
		Escribir 'El orden de los datos ascendente es: [',dato3,'][',dato2,'][',dato1,']'
	SiNo
		Si dato3>dato2 Y dato2>dato1 Entonces
			Escribir 'El orden de los datos ascendente es: [',dato1,'][',dato2,'][',dato3,']'
		SiNo
			Si dato2>dato1 Y dato1>dato3 Entonces
				Escribir 'El orden de los datos ascendente es: [',dato3,'][',dato1,'][',dato2,']'
			SiNo
				Si dato3>dato1 Y dato1>dato2 Entonces
					Escribir 'El orden de los datos ascendente es: [',dato2,'][',dato1,'][',dato3,']'
				SiNo
					Si dato1>dato3 Y dato3>dato2 Entonces
						Escribir 'El orden de los datos ascendente es: [',dato2,'][',dato3,'][',dato1,']'
					SiNo
						Escribir 'El orden de los datos ascendente es: [',dato1,'][',dato3,'][',dato2,']'
					FinSi
				FinSi
			FinSi
		FinSi
	FinSi
FinAlgoritmo
