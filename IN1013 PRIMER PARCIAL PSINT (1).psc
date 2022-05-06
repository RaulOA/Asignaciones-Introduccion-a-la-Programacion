Algoritmo ejercicio_a
	
	//Realizar un algoritmo en diagrama de flujo que solicite en pantalla el nombre de usuario y una contraseña. 
	//Si el nombre es "pepe" y la contraseña es "supercontraseña", mostrar en pantalla "Usuario y contraseña correctos. 
	//Puede ingresar al sistema super". Si el nombre o la contraseña no coinciden, mostrar "Acceso denegado". Intente de nuevo, 
	//ademas es importante recalcar que solo debe de permitir 3 intentos para ingresar al sistema, 
	//si el usuario falla los 3 intentos debe de mostrar "Sistema bloqueado, consulte con el administrador" Valor 5 puntos
	
	Definir usuario Como Caracter
	usuario<-""
	Definir pass Como Caracter
	pass<-""
	Definir usuariocreado Como Caracter
	usuariocreado<-""
	Definir passcreada Como Caracter
	passcreada<-""
	Definir intentos Como Entero
	intentos<-3
	
	Escribir "OK... Vamos a crear una nueva cuenta"
	
	Escribir "Porfavor ingresa un nombre para su nuevo usuario"
	Leer usuario
	Escribir "Ahora ingresa tu nueva Contraseña [Guarda esta contraseña]"
	Leer pass
	
	Escribir "Ahora vamos a verificar sus datos"
	
	Escribir "Ingrese su Usuario"
	Leer usuariocreado
	
	Repetir
		
		Si usuariocreado<>usuario Entonces
			Escribir "Usuario Incorrecto, Ingrese nuevamente"
			Leer usuariocreado
		Fin Si
		
	Hasta Que usuariocreado==usuario
		
	Escribir "Correcto!! Ahora ingrese su contraseña"
	Leer passcreada
	
	Repetir
		
		Si passcreada<>pass Entonces
			intentos<-intentos-1
			Escribir "Acceso denegado, Intente de nuevo, Intentos Restantes: ",intentos
			Leer passcreada
		Fin Si
		
	Hasta Que passcreada==pass o intentos==1
	
	Si passcreada<>pass Entonces
		Escribir "Sistema bloqueado, consulte con el administrador"
	SiNo
		Escribir "Usuario y contraseña correctos. Puede ingresar al sistema"
	Fin Si
	
FinAlgoritmo
