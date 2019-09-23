Proceso sin_titulo
	//inputs
	Escribir "Dame la edad que tienes"
	leer edad	
	//Proceso 
	si edad <= 12
		Escribir "puedes verlas peliculas aptas para todo el publico"
	SiNo
		si edad <= 17
			Escribir " puedes ver las peliculas de clasificacion B"
		SiNo
			si edad >= 18
				Escribir "pudes ver las peliculas clasificacion C"
			FinSi
		FinSi
	FinSi
FinProceso
