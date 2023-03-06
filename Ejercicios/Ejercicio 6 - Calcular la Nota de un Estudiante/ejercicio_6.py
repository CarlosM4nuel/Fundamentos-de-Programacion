# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Calcula la nota definitiva de un estudiante y lo aprueba o reprueba con la condicion que se asista x veces
	# Desarrollador: Carlos Manuel Muñoz
	# Fecha de Desarrollo: 25/02/2023
	# Version: 1.0
	# AREA DE DECLARACION DE VARIABLES
	inasistencia = float()
	parcial_1 = float()
	parcial_2 = float()
	parcial_3 = float()
	p_p_1 = float()
	p_p_2 = float()
	p_p_3 = float()
	estudiante = str()
	materia = str()
	# AREA DE CAPTURA DE DATOS
	print(" Digite su nombre ")
	estudiante = input()
	print(" Digite el nombre de la materia ")
	materia = input()
	print("Digite la nota del parcial 1 ")
	parcial_1 = float(input())
	print(" Porcentaje parcial 1 ")
	p_p_1 = float(input())
	print(" Digite la nota del parcial 2 ")
	parcial_2 = float(input())
	print(" Porcentaje parcial 2 ")
	p_p_2 = float(input())
	print(" Digite la nota del parcial 3 ")
	parcial_3 = float(input())
	print(" Porcentaje parcial 3 ")
	p_p_3 = float(input())
	print(" Cuantas veces falto a clase ")
	inasistencia = float(input())
	# AREA DE PROCESOS 
	notas = ((parcial_1/100)*p_p_1)+((parcial_2/100)*p_p_2)+((parcial_3/100)*p_p_3)
	if inasistencia>12:
		print("Reprobo por inasistencia")
	else:
		print("Asistio cumplidamente")
		if notas<3.4:
			print("Reprobo")
		else:
			print("Aprobo")
	# AREA DE SALIDAS
	print("Su nota definitiva es: ",notas)

