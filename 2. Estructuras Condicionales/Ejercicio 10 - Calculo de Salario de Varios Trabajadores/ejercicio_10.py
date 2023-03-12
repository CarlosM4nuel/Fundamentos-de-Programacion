# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Area de documentacion
	# enunciado: Calculo del salario de empleados basados en las horas trabajadas
	# version: 1.0
	# desarrollado por: Carlos Manuel Muñoz
	# fecha: 23/02/2023
	# Area de definicion de variables
	# Variable que va a almacenar las horas trabajadas del empleado
	horas_trabajadas = float()
	# Variable que almacenara el precio de la hora trabajada
	precio_hora = float()
	# Variable que almacenara el salario del empleado
	salario = float()
	# Variable que almacera el nombre del empleado
	nombre_empleado = str()
	# Variable para almacenar mas trabajadores en caso de continuar
	mas_datos = str()
	# Area de procesos y entrada de datos
	while True:# no hay 'repetir' en python
		print("Nombre del Empleado:")
		nombre_empleado = input()
		print("Digite las Horas Trabajadas:")
		horas_trabajadas = float(input())
		print("Digite el Precio de la Hora")
		precio_hora = float(input())
		if horas_trabajadas<=40:
			salario = horas_trabajadas*precio_hora
		else:
			salario = 40*precio_hora+1.5*(horas_trabajadas-40)*precio_hora
		# Area de salidas
		print("Empleado: ",nombre_empleado)
		print("El Salario del Empleado: ",nombre_empleado," es: ",salario)
		print("¿Desea anotar otro trabajador?: ")
		mas_datos = input()
		if mas_datos=="N": break

