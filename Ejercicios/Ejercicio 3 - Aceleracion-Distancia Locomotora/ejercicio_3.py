# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Programa que en base a la formula A=(VF-VI)/T - d=vi*t+1/2*a*t^2 calcula la aceleracion y distancia recorrida de una locomotora
	# Desarrollador: Carlos Manuel Muñoz
	# Fecha de Desarrollo: 20/02/2023
	# Version: 1.0
	# AREA DE DECLARAR VARIABLES, v_velini(VELOCIDADINICIAL), v_velfin(VELOCIDADFINAL), v_tiempo(TIEMPO), v_distancia(DISTANCIA), v_aceleracion(ACELERACION)
	v_velini = float()
	v_velfin = int()
	v_aceleracion = float()
	v_tiempo = int()
	v_distancia = float()
	# AREA DE ASIGNACION DE DATOS
	print("Ingrese la Velocidad Inicial:")
	v_velini = float(input())
	print("Ingrese la Velocidad Final:")
	v_velfin = int(input())
	print("Ingrese el Tiempo:")
	v_tiempo = int(input())
	# AREA DE OPERACIONES ARITMETICAS APLICANDO FORMULA A=(VF-VI)/T para ACELERACION
	v_aceleracion = (v_velfin-v_velini)/v_tiempo
	# AREA DE OPERACIONES ARITMETICAS APLICANDO FORMULA D=VI*T+1/2*A*T^2 para DISTANCIA
	v_distancia = v_velini*v_tiempo+1/2*v_aceleracion*v_tiempo**2
	# AREA DE RESULTADO DEL PROCESO ARITMETICO Y FIN DEL ALGORITMO
	print("La Aceleracion de la Locomotora es: ",v_aceleracion,"m/s")
	print("La Distancia recorrida por la Locomotora son: ",v_distancia,"m")

