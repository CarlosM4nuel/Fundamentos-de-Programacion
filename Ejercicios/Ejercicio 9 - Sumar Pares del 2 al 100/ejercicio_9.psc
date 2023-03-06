Algoritmo sin_titulo
	//Area de documentacion
	//enunciado: Suma de Numeros Pares entre el 2 y el 100
	//version: 1.0
	//desarrollado por: Carlos Manuel Muñoz
	//fecha: 23/02/2023
	
	//Area de definicion de variables
	Definir nmero Como Entero
	suma = 2 //Variable que ira sumando de 2 en 2 para que sean pares
	nmero = 4 //Variable desde la cual inicia a sumar de par en par 
	
	//Area de procesos
	mientras (nmero <= 100) hacer
		suma <- suma + nmero
		nmero <- nmero + 2
	fin mientras
	
	//Area de salidas
	Escribir 'Suma pares entre 2 y 100: ', suma
FinAlgoritmo
