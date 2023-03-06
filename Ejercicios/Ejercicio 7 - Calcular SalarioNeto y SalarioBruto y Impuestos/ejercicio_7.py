# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Area de documentacion
	# enunciado: Calculo del Salario Bruto y Salario Neto en base a la horas trabajadas restandole los impuestos a pagar
	# version: 1.0
	# desarrollado por: Carlos Manuel Muñoz
	# fecha: 24/02/2023
	# Area de definicion de variables
	# Variable que almacenara las horas semanales trabajadas por X empleado
	horas_trabajadas = float()
	# Variable que almacenara el valor de la hora de trabajo de X empleado
	precio_hora = float()
	# Variable que almacenara el nombre del empleado a realizar el proceso
	nombre_empleado = str()
	# Area de entradas
	print("Digite el Nombre del Empleado")
	nombre_empleado = input()
	print("Digite las Horas Trabajadas")
	horas_trabajadas = float(input())
	print("Digite el Precio de la Hora")
	precio_hora = float(input())
	# Area de procesos
	salario_bruto = horas_trabajadas*precio_hora
	impuestos = 0.25*salario_bruto
	salario_neto = salario_bruto-impuestos
	# Area de salidas
	print("Nombre del Empleado: ",nombre_empleado)
	print("Las Horas Trabajadas por ",nombre_empleado," son: ",horas_trabajadas)
	print("Los Impuestos a Descontar son: ",impuestos)
	print("Su Salario Bruto es: ",salario_bruto)
	print("Su Salario Neto es: ",salario_neto)

