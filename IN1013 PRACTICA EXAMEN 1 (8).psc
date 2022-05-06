Algoritmo practica_10_examen
	Escribir "Nombre del Cliente"
	Leer nombre
	Escribir "Nombre del producto"
	Leer producto
	Escribir "Precio del producto"
	leer precio
	tipo<-""
	Repetir
		Escribir "Tipo de cliente [A=40%] [B=30%] [C=5%] de descuento"
		leer tipo
		Si tipo=="A" Entonces
			descuento<-(precio*40)/100
			preciofinal<-precio-descuento
		SiNo
			Si tipo=="B" Entonces
				descuento<-(precio*30)/100
				preciofinal<-precio-descuento
			SiNo
				Si tipo=="C" Entonces
					descuento<-(precio*5)/100
					preciofinal<-precio-descuento
				SiNo
					Escribir "Opcion Incorrecta.Digite A, B o C"
				Fin Si
			Fin Si
		Fin Si
	Hasta Que tipo=="A" o tipo=="B" o tipo=="C"
	Escribir "Nombre del Cliente: ",nombre
	Escribir "Tipo del Cliente: ",tipo
	Escribir "Nombre del Producto: ",producto
	Escribir "Precio del producto original: ",precio
	Escribir "Precio con descuento: ",preciofinal
	FinAlgoritmo
