Algoritmo sin_titulo
	//Area de documentacion
	//enunciado: Calcular la media de una serie de números positivos
	//version: 1.0
	//desarrollado por: Carlos Manuel Muñoz
	//fecha: 23/02/2023
	
	//Area de definicion de variables
	Definir contador_numeros Como Entero //Variable que almacenara los numeros digitados e ira sumandoles 1
	Definir suma_numeros Como Real //Variable que ira sumando los numeros digitados
	
	//Area de entradas
	Escribir "Digite los numeros:  (Para finalizar el proceso introduce 0)"
	Repetir
		Leer num
		si num <> 0 Entonces
			contador_numeros = contador_numeros + 1   //Area de procesos
			suma_numeros = suma_numeros + num        //Area de procesos
		FinSi 
	Hasta Que num = 0
	si (contador_numeros > 0) Entonces              //Area de procesos
		media = suma_numeros/contador_numeros        //Area de procesos
		//Area de salidas
		Escribir "La Media es: " media
	FinSi
FinAlgoritmo
