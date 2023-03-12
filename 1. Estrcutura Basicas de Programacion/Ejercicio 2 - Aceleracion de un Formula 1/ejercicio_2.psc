Algoritmo ejercicio_2
	//Programa que en base a la formula A=(VF-VI)/T calcula la aceleracion de un formula 1//
	//Desarrollador: Carlos Manuel Muñoz//
	//Fecha de Desarrollo: 20/02/2023//
	//Version: 1.0//
	//AREA DE DEFINICION DE VARIABLES, v_velIni(VELOCIDADINICIAL), v_velFin(VELOCIDADFINAL), v_Tiempo(TIEMPO), aceleracion(ACELERACION)//
	Definir v_velIni Como Entero;
	Definir v_velFin Como Entero;
	Definir v_Tiempo Como Entero;
	Definir v_transkm_ms Como Entero;
	Definir aceleracion Como Real;
	
	//AREA DE ASIGNACION DE DATOS//
	Escribir "Digite la velocidad Inicial"; Leer v_velIni;
	Escribir "Digite la velocidad Final"; Leer v_velFin;
	Escribir "Digite el Tiempo"; Leer v_Tiempo;
	
	//AREA DE TRANSFORMACION DE KM/H -> M/S FORMULA: VF*1000/3600//
	v_transkm_ms = (v_velFin*1000)/3600
	
	//AREA DE OPERACIONES ARITMETICAS APLICANDO FORMULA A=(VF-VI)/T//
	aceleracion = (v_transkm_ms-v_velIni)/v_Tiempo
	
	//AREA DE RESULTADO DEL PROCESO ARITMETICO Y FIN DEL ALGORITMO//
	Escribir "La aceleracion es: " aceleracion " m/s2"
FinAlgoritmo
