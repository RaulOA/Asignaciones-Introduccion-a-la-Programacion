Algoritmo ejercicio_d
	
	//Realice un algoritmo en diagrama de flujo o en pseudocodigo este debe de registrar las horas 
	//que trabaja diariamente una persona durante la semana esta solo trabaja 6 días de la semana y requiere determinar 
	//el total de éstas, así como el sueldo que recibirá por las horas trabajadas. Solucione el algoritmo. Valor 5 puntos Usar Ciclo
	
	dia<-1
	horastotales<-0
	horasdia<-0
	
	Mientras dia<7 Hacer
		
		Escribir "Digite las horas trabajadas del dia #",dia
		leer horasdia
		horastotales<-horastotales+horasdia
		dia<-dia+1
		
	Fin Mientras
	
	Escribir "Ahora, Digita el (Precio x Hora) en $"
	Leer precio
	
	salario<-horastotales*precio
	
	Escribir "Esta semana trabajaste:",horastotales," horas y tu salario es de: $",salario
	
FinAlgoritmo
