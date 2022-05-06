Algoritmo Ejercicio_6
	// Una farmacia tiene puntos de venta de vacunas que se pretende funcionen de la siguiente manera. 
	// Cada día, empezar con 1000 vacunas disponibles y a través de un programa que controla las 
	// entregas avisar si el inventario baja de 200 unidades.
	vacunas<-1000
	Escribir "Hola, usted esta comenzando con un numero maximo de 1000 vacunas para el dia de hoy"
	Repetir
		Escribir "Digite 1 para Ingresar Entrega o 2 para salir del programa "
		Leer respuesta
			si respuesta==1
				Entonces
				Escribir "Nombre del Cliente"
				Leer cliente
				Escribir "Cantidad de vacunas que necesita el cliente"
				Leer enviado
				vacunas<-vacunas-enviado
				Escribir "Vacunas restantes = ",vacunas
			SiNo
				si respuesta==2
					Escribir "Gracias por utilizar nuestro programa, sus vacunas seran restauradas a 1000 unidades"
				SiNo
					Escribir "La Opcion Ingresada no es Valida, Intente Nuevamente!!"
			FinSi
		FinSi
		si vacunas<=200&&respuesta==1
			Entonces
			Escribir "AVISO IMPORTANTE: Le quedan ",vacunas," vacunas en su inventario"
		SiNo			
		FinSi
	Hasta Que respuesta==2
	vacunas<-1000
	Escribir "Escrito por: Sebastian Naranjo, David Porras y Raul Ortega"
FinAlgoritmo
