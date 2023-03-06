Algoritmo sin_titulo
	//Area de documentacion
	//enunciado: Determinacion de la cantidad total a pagar por una llamada telefonica
	//version: 1.0
	//desarrollado por: Carlos Manuel Muñoz
	//fecha: 23/02/2023
	
	//Area de definicion de variables
	Definir n_pasos Como real //Variable que almacena el numero de pasos de la llamada
	Definir fact como real 
	
	//Area de entrada de datos
	Escribir "Ingrese el numero de pasos de la llamada: "
	Leer  n_pasos
	
	//Area de procesos
	Si n_pasos <= 0 Entonces
		Escribir "NO SE PUEDE REALIZAR ESTA ACCION"
	SiNo
		fact = 10
		n = n_pasos-5
		si n > 0 Entonces
			fact = fact + n * 5
			sino 
		FinSi 
	Fin Si 
	
	//Area de salidas
	Escribir "Numero de pasos de la llamada: " n_pasos
	Escribir "El Precio de la llamada es: " fact
	Escribir "Número de pasos que exceden a 5: " n
FinAlgoritmo
