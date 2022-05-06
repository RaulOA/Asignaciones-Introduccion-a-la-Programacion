Algoritmo practiva_9_examen
	cantidad<-0
	Repetir
		Escribir "Escriba su mes de nacimiento 1-12"
		Leer mes
		Si mes>=1 y mes<=12 Entonces
			Si mes==1 Entonces
				cantidad<-cantidad+0
			SiNo
				Si mes==2 Entonces
					cantidad<-cantidad+31
				SiNo
					Si mes==3 Entonces
						cantidad<-cantidad+59
					SiNo
						Si mes==4 Entonces
							cantidad<-cantidad+90
						SiNo
							Si mes==5 Entonces
								cantidad<-cantidad+120
							SiNo
								Si mes==6 Entonces
									cantidad<-cantidad+151
								SiNo
									Si mes==7 Entonces
										cantidad<-cantidad+181
									SiNo
										Si mes==8 Entonces
											cantidad<-cantidad+212
										SiNo
											Si mes==9 Entonces
												cantidad<-cantidad+243
											SiNo
												Si mes==10 Entonces
													cantidad<-cantidad+273
												SiNo
													Si mes==11 Entonces
														cantidad<-cantidad+304
													SiNo
														Si mes==12 Entonces
															cantidad<-cantidad+334
														Fin Si
													Fin Si
												Fin Si
											Fin Si
										Fin Si
									Fin Si
								Fin Si
							Fin Si
						Fin Si
					Fin Si
				Fin Si
			Fin Si
		SiNo
			Escribir "Digite un mes valido del 1 al 12"
		Fin Si
	Hasta Que mes>=1 y mes<=12
	Escribir "Escriba su dia de nacimie1nto en numero"
	leer dia
	cantidad<-cantidad+dia
	Escribir "Dia del año ",cantidad
	Si cantidad>=80 y cantidad<=110 Entonces
		Escribir "Su signo es: Aries - 21 de marzo al 20 de abril"
	SiNo
		Si cantidad>=111 y cantidad<=141 Entonces
			Escribir "Su signo es: Tauro - 21 de abril al 21 de mayo"
		SiNo
			Si cantidad>=142 y cantidad<=172 Entonces
				Escribir "Su signo es: Géminis - 22 de mayo al 21 de junio"
			SiNo
				Si cantidad>=173 y cantidad<=203 Entonces
					Escribir "Su signo es: Cáncer - 22 de junio al 22 de julio"
				SiNo
					Si cantidad>=204 y cantidad<=234 Entonces
						Escribir "Su signo es: Leo - 23 de julio al 22 de agosto"
					SiNo
						Si cantidad>=235 y cantidad<=265 Entonces
							Escribir "Su signo es: Virgo - 23 de agosto al 22 de septiembre"
						SiNo
							Si cantidad>=266 y cantidad<=295 Entonces
								Escribir "Su signo es: Libra - 23 de septiembre al 22 de octubre"
							SiNo
								Si cantidad>=296 y cantidad<=326 Entonces
									Escribir "Su signo es: Escorpio - 23 de octubre al 22 de noviembre"
								SiNo
									Si cantidad>=327 y cantidad<=355 Entonces
										Escribir "Su signo es: Sagitario - 23 de noviembre al 21 de diciembre"
									SiNo
										Si cantidad>=356 y cantidad<=365 o cantidad>=1 y cantidad<=20 Entonces
											Escribir "Su signo es: Capricornio -	22 de diciembre al 20 de enero"
										SiNo
											Si cantidad>=21 y cantidad<=49 Entonces
												Escribir "Su signo es: Acuario - 21 de enero al 18 de febrero"
											SiNo
												Si cantidad>=50 y cantidad<=79 Entonces
													Escribir "Su signo es: Piscis - 19 de febrero al 20 de marzo"
												Fin Si
											Fin Si
										Fin Si
									Fin Si
								Fin Si
							Fin Si
						Fin Si
					Fin Si
				Fin Si
			Fin Si
		Fin Si
	Fin Si
	//Signo	Fechas	Días
	//Aries	21 de marzo al 20 de abril	31
	//Tauro	21 de abril al 21 de mayo	31
	//Géminis	22 de mayo al 21 de junio	31
	//Cáncer	22 de junio al 22 de julio	31
	//Leo	23 de julio al 22 de agosto	31
	//Virgo	23 de agosto al 22 de septiembre	31
	//Libra	23 de septiembre al 22 de octubre	30
	//Escorpio	23 de octubre al 22 de noviembre	31
	//Sagitario	23 de noviembre al 21 de diciembre	29
	//Capricornio	22 de diciembre al 20 de enero	30
	//Acuario	21 de enero al 18 de febrero	29
	//Piscis	19 de febrero al 20 de marzo	30/31
FinAlgoritmo
