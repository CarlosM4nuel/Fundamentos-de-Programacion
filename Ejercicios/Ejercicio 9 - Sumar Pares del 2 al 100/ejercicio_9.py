# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Area de documentacion
	# enunciado: Suma de Numeros Pares entre el 2 y el 100
	# version: 1.0
	# desarrollado por: Carlos Manuel Muñoz
	# fecha: 23/02/2023
	# Area de definicion de variables
	nmero = int()
	# Variable que ira sumando de 2 en 2 para que sean pares
	suma = 2
	# Variable desde la cual inicia a sumar de par en par 
	nmero = 4
	# Area de procesos
	while (nmero<=100):
		suma = suma+nmero
		nmero = nmero+2
	# Area de salidas
	print("Suma pares entre 2 y 100: ",suma)

