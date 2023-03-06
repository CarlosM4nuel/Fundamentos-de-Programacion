# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Programa que en base a la formula T=(VF-VI)/A calcula el tiempo que demora en llegar a 144km/h//
	# Desarrollador: Carlos Manuel Muñoz//
	# Fecha de Desarrollo: 20/02/2023//
	# Version: 1.0//
	# AREA DE DEFINICION DE VARIABLES, VI(VELOCIDADINICIAL), VF(VELOCIDADFINAL), A(ACELERACION), T(TIEMPO), M(CAMBIO DE KM/H->M/S//
	v_velini = int()
	v_velfin = int()
	v_aceleracion = int()
	v_tiempo = int()
	v_transkmh_ms = int()
	# AREA DE ASIGNACION DE DATOS//
	print("Digite la Velocidad Inicial")
	v_velini = int(input())
	print("Digite la Velocidad Final")
	v_velfin = int(input())
	print("Digite la Aceleracion")
	v_aceleracion = int(input())
	# AREA DE OPERACIONES ARITMETICAS APLICANDO FORMULA M=(VF*1000)/3600 para TRANSFORMAR KM/H -> M/S//
	v_transkmh_ms = v_velfin*(1000/3600)
	# AREA DE OPERACIONES ARITMETICAS APLICANDO FORMULA T=(VF-VI)/A para ACELERACION//
	v_tiempo = (v_transkmh_ms-v_velini)/v_aceleracion
	# AREA DE RESULTADO DEL PROCESO ARITMETICO Y FIN DEL ALGORITMO//
	print("El tiempo que tarda es: ",v_tiempo," Segundos")

