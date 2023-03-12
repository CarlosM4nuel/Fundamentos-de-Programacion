# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Area de documentacion
	# enunciado: Calcular la media de una serie de números positivos
	# version: 1.0
	# desarrollado por: Carlos Manuel Muñoz
	# fecha: 23/02/2023
	# Area de definicion de variables
	# Variable que almacenara los numeros digitados e ira sumandoles 1
	contador_numeros = int()
	# Variable que ira sumando los numeros digitados
	suma_numeros = float()
	# Area de entradas
	print("Digite los numeros:  (Para finalizar el proceso introduce 0)")
	while True:# no hay 'repetir' en python
		num = float(input())
		if num!=0:
			# Area de procesos
			contador_numeros = contador_numeros+1
			# Area de procesos
			suma_numeros = suma_numeros+num
		if num==0: break
	# Area de procesos
	if (contador_numeros>0):
		# Area de procesos
		media = suma_numeros/contador_numeros
		# Area de salidas
		print("La Media es: ",media)

