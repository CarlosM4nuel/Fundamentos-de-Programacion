Algoritmo ejercicio_3
	//Programa que en base a la formula A=(VF-VI)/T - d=vi*t+1/2*a*t^2 calcula la aceleracion y distancia recorrida de una locomotora
	//Desarrollador: Carlos Manuel Muñoz
	//Fecha de Desarrollo: 20/02/2023
	//Version: 1.0
	//AREA DE DECLARAR VARIABLES, v_velini(VELOCIDADINICIAL), v_velfin(VELOCIDADFINAL), v_tiempo(TIEMPO), v_distancia(DISTANCIA), v_aceleracion(ACELERACION)
    Definir v_velini como Real;
	Definir v_velfin Como Entero;
	Definir v_aceleracion Como Real;
	Definir v_tiempo Como Entero;
	Definir v_distancia Como Real;
	
	//AREA DE ASIGNACION DE DATOS
	Escribir "Ingrese la Velocidad Inicial:"; Leer v_velini;
	Escribir "Ingrese la Velocidad Final:"; Leer v_velfin;
	Escribir "Ingrese el Tiempo:"; Leer v_tiempo;
	
	//AREA DE OPERACIONES ARITMETICAS APLICANDO FORMULA A=(VF-VI)/T para ACELERACION
	v_aceleracion = (v_velfin - v_velini)/v_tiempo
	
	//AREA DE OPERACIONES ARITMETICAS APLICANDO FORMULA D=VI*T+1/2*A*T^2 para DISTANCIA
	v_distancia = v_velini * v_tiempo + 1/2 * v_aceleracion * v_tiempo ^ 2
	
	//AREA DE RESULTADO DEL PROCESO ARITMETICO Y FIN DEL ALGORITMO
	Escribir "La Aceleracion de la Locomotora es: " v_aceleracion "m/s";
	Escribir "La Distancia recorrida por la Locomotora son: " v_distancia "m";
FinAlgoritmo