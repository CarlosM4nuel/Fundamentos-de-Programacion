Algoritmo ejercicio_4
	//Programa que en base a la formula T=(VF-VI)/A calcula el tiempo que demora en llegar a 144km/h//
	//Desarrollador: Carlos Manuel Muñoz//
	//Fecha de Desarrollo: 20/02/2023//
	//Version: 1.0//
	//AREA DE DEFINICION DE VARIABLES, VI(VELOCIDADINICIAL), VF(VELOCIDADFINAL), A(ACELERACION), T(TIEMPO), M(CAMBIO DE KM/H->M/S//
	Definir v_velini Como Entero;
	Definir v_velfin Como Entero;
	Definir v_aceleracion Como Entero;
	Definir v_tiempo Como Entero;
	Definir v_transkmh_ms Como Entero;
	
	//AREA DE ASIGNACION DE DATOS//
	Escribir "Digite la Velocidad Inicial"; Leer  v_velini
	Escribir "Digite la Velocidad Final"; Leer v_velfin
	Escribir "Digite la Aceleracion"; Leer v_aceleracion
	
	//AREA DE OPERACIONES ARITMETICAS APLICANDO FORMULA M=(VF*1000)/3600 para TRANSFORMAR KM/H -> M/S//
	v_transkmh_ms = v_velfin * (1000/3600)
	
	//AREA DE OPERACIONES ARITMETICAS APLICANDO FORMULA T=(VF-VI)/A para ACELERACION//
	v_tiempo = (v_transkmh_ms-v_velini)/v_aceleracion
	
	//AREA DE RESULTADO DEL PROCESO ARITMETICO Y FIN DEL ALGORITMO//
	Escribir "El tiempo que tarda es: " v_tiempo " Segundos"
FinAlgoritmo
