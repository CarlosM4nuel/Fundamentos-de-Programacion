# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Area de documentacion
	# enunciado: Suma de los primeros 50 numeros enteros
	# version: 1.0
	# desarrollado por: Carlos Manuel Muñoz
	# fecha: 23/02/2023
	# Area de definicion de variables
	suma = int()
	# Variable que ira sumando de 1 en 1 los 50 primeros numeros enteros
	nmero = 1
	# Variable desde la cual inicia a sumar de 1 en 1
	suma = 2
	# Area de procesos
	while (suma<=50):
		nmero = nmero+suma
		suma = suma+1
	# Area de salidas
	print("La suma de los primeros 50 numeros enteros es: ",nmero)

