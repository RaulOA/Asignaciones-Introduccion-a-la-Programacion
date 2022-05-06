Algoritmo practica_11_examen
	//Diseñe un Algoritmo que solicite 15 números, de estos se debe de obtener su promedio, 
	//el mayor y menor de esos números y mostrarlos en pantalla.
	Dimension num[15]
	flecha1<-1
	flecha2<-2
	aux<-0
	acumulador<-0
	
	Repetir
		Escribir "digite el dato #",flecha1
		Leer num[flecha1]
		flecha1<-flecha1+1
	Hasta Que flecha1==16
	
	contador<-0
	flecha1<-1
	
	aux<-num[1]+num[2]+num[3]+num[4]+num[5]+num[6]+num[7]+num[8]+num[9]+num[10]+num[11]+num[12]+num[13]+num[14]+num[15]
		
	Escribir "La Suma total es de:",aux," y su Promedio es: ",aux/15
	
	Repetir
		Si num[flecha1]>num[flecha2] Entonces
			aux<-num[flecha1]
			num[flecha1]<-num[flecha2]
			num[flecha2]<-aux
			flecha1<-flecha1+1
			flecha2<-flecha2+1
			acumulador<-acumulador+1
		SiNo
			flecha1<-flecha1+1
			flecha2<-flecha2+1
		Fin Si
	Hasta Que expresion_logica
FinAlgoritmo
