Algoritmo ejercicio_1
	//Programa que en base a la formula A=(VF-VI)/T calcula la aceleracion de un camion//
	//Desarrollador: Carlos Manuel Muñoz//
	//Fecha de Desarrollo: 20/02/2023//
	//Version: 1.0//
	//AREA DE DEFINICION DE VARIABLES, v_velIni(VELOCIDADINICIAL), v_velFin(VELOCIDADFINAL), v_Tiempo(TIEMPO), aceleracion(ACELERACION)//
	Definir v_velFin Como Entero;
	Definir v_velIni Como Entero;
	Definir v_Tiempo Como Entero;
	Definir aceleracion Como Entero
	//AREA DE ASIGNACION DE DATOS//
	Escribir "Digite la Velocidad Inicial"; Leer v_velIni;
	Escribir "Digite la Velocidad Final"; Leer v_velFin;
	Escribir "Digite el Tiempo"; Leer v_Tiempo;
	//AREA DE OPERACIONES ARITMETICAS APLICANDO FORMULA A=(VF-VI)/T//
	aceleracion = (v_velFin - v_velIni) / v_Tiempo
	//AREA DE RESULTADO DEL PROCESO ARITMETICO Y FIN DEL ALGORITMO//
	Escribir "Su resultado es: " aceleracion "m/s2";
FinAlgoritmo
