Algoritmo sin_titulo
	
	//Area de documentacion
	//enunciado: Suma de los primeros 50 numeros enteros
	//version: 1.0
	//desarrollado por: Carlos Manuel Muñoz
	//fecha: 23/02/2023
	
	//Area de definicion de variables
	Definir suma Como Entero
	nmero = 1 //Variable que ira sumando de 1 en 1 los 50 primeros numeros enteros
	suma = 2 //Variable desde la cual inicia a sumar de 1 en 1
	
	//Area de procesos
	mientras (suma <= 50) hacer
		nmero <- nmero + suma
		suma <- suma + 1
	fin mientras
	
	//Area de salidas
	Escribir 'La suma de los primeros 50 numeros enteros es: ', nmero
FinAlgoritmo
