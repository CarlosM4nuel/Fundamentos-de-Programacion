# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Area de documentacion
	# enunciado: Determinacion de la cantidad total a pagar por una llamada telefonica
	# version: 1.0
	# desarrollado por: Carlos Manuel Muñoz
	# fecha: 23/02/2023
	# Area de definicion de variables
	# Variable que almacena el numero de pasos de la llamada
	n_pasos = float()
	fact = float()
	# Area de entrada de datos
	print("Ingrese el numero de pasos de la llamada: ")
	n_pasos = float(input())
	# Area de procesos
	if n_pasos<=0:
		print("NO SE PUEDE REALIZAR ESTA ACCION")
	else:
		fact = 10
		n = n_pasos-5
		if n>0:
			fact = fact+n*5
		else:
	# Area de salidas
	print("Numero de pasos de la llamada: ",n_pasos)
	print("El Precio de la llamada es: ",fact)
	print("Número de pasos que exceden a 5: ",n)

