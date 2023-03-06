# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Programa que en base a la formula A=(VF-VI)/T calcula la aceleracion de un camion//
	# Desarrollador: Carlos Manuel Muoz//
	# Fecha de Desarrollo: 20/02/2023//
	# Version: 1.0//
	# AREA DE DEFINICION DE VARIABLES, v_velIni(VELOCIDADINICIAL), v_velFin(VELOCIDADFINAL), v_Tiempo(TIEMPO), aceleracion(ACELERACION)//
	v_velfin = int()
	v_velini = int()
	v_tiempo = int()
	aceleracion = int()
	# AREA DE ASIGNACION DE DATOS//
	print("Digite la Velocidad Inicial")
	v_velini = int(input())
	print("Digite la Velocidad Final")
	v_velfin = int(input())
	print("Digite el Tiempo")
	v_tiempo = int(input())
	# AREA DE OPERACIONES ARITMETICAS APLICANDO FORMULA A=(VF-VI)/T//
	aceleracion = (v_velfin-v_velini)/v_tiempo
	# AREA DE RESULTADO DEL PROCESO ARITMETICO Y FIN DEL ALGORITMO//
	print("Su resultado es: ",aceleracion,"m/s2")

