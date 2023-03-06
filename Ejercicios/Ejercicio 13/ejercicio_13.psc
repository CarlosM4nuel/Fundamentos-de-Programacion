Algoritmo sin_titulo
	
	//Area de documentacion
	//enunciado: Calcular el producto N * (N - 1 * (n - 2) * ... * 3 * 2 * 1
	//version: 1.0
	//desarrollado por: Carlos Manuel Muñoz
	//fecha: 23/02/2023
	
	//Area de definicion de variables
	Definir N Como Entero
	Definir P Como Real
	Leer N
	
	//Area de procesos
	Si N = 0 Entonces
		Escribir "Factorial de 0 igual a 1"
		si N > 0 Entonces
			P <- 1
			P <- P * N
			N <- N - 1
			Si N = 1 Entonces
				Escribir "Factorial =", P
			FinSi
		SiNo
			
	//Area de salidas
	Escribir "Numeros Negativos"
	Escribir "Pruebe con Positivos"
		FinSi
	FinSi
FinAlgoritmo
	