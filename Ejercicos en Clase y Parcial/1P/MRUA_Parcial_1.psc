Proceso MRUA_Parcial_1
	
	//
	//Desarrollado por Carlos Muñoz y Jhon Mario Tabares
	//Fecha: 13/03/2023
	//Versión 1.0
	
	//Definición de variables 
	Definir v_VelInc, v_VelFin,v_Tiem, v_VelMed, v_Dis, v_OpcVelIns Como Real
	Definir v_Opc Como Entero
	
	//Inicializacion de variables
	v_Opc = 0
	v_VelInc = 0.0
	v_VelFin = 0.0
	v_VelMed = 0.0
	v_Tiem = 0.0
	v_Dis = 0.0
	v_OpcVelIns = 0.0
	
	//Entrada de datos
	Escribir " Elija una opción: "
	Escribir "1-Para hallar la velocidad media"
	Escribir "2- Calculos de velocidad instantanea"
	Escribir "3- Salir"
	Leer v_Opc
	Limpiar Pantalla
	
	//Procesos
	Si v_Opc = 1 Entonces
		Escribir " Digite la velocidad inicial" 
		Leer v_VelInc 
		Escribir "Digite la velocidad final"
		Leer v_VelFin
		v_VelMed = (v_VelFin + v_VelInc) / 2
		Escribir " La velocidad media es: ",v_VelMed
	Fin Si
	Si v_Opc = 2 Entonces
		Escribir "2.1- Hallar la aceleracion"
		Escribir "2.2- Hallar la velocidad final" 
		Escribir "2.3- Hallar la velocidad final al cuadrado"
		Escribir "2.4- Hallar la distancia" 
		Leer v_OpcVelIns
		
	FinSi
	si v_OpcVelIns = 2.1 Entonces
		Escribir "Digite la velocidad inicial"
		leer v_VelInc
		Escribir "Digite la velocidad final"
		Leer v_VelFin
		Escribir "Digite el tiempo"
		Leer v_Tiem
		v_Ace = (v_VelFin - v_VelInc) / v_Tiem
		Escribir " La aceleración es: ", v_Ace ," m/s2 "
		
	FinSi
	si v_OpcVelIns = 2.2 Entonces
		Escribir "Digite la velocidad inicial"
		leer v_VelInc
		Escribir " Digite la aceleración "
		Leer v_Ace
		Escribir "Digite el tiempo"
		Leer v_Tiem
		v_VelFin = v_VelInc + (v_Ace * v_Tiem)
		Escribir " La velocidad final es: ", v_VelFin
		
	FinSi
	Si v_OpcVelIns = 2.3 Entonces
		Escribir " Digite la velocidad inicial "
		Leer v_VelInc
		Escribir " Digite la aceleracion"
		Leer v_Ace
		Escribir " Digite la distancia"
		Leer v_Dis
		v_VelFin2 = (v_VelInc^2) + 2 * v_Ace * v_Dis
		Escribir "La velocidad final al cuadrado es: ", v_VelFin2
	FinSi
	Si v_OpcVelIns = 2.4 Entonces
		Escribir " Digite la velocidad inicial"
		Leer v_VelInc
		Escribir " Digite la velocidad final "
		Leer v_VelFin
		Escribir "Digite el tiempo"
		Leer v_Tiem
		v_Dis = (v_VelFin + v_VelInc / 2) *v_Tiem
		Escribir "La distancia es: " v_Dis
	FinSi
	Si v_Opc = 3 Entonces
		Escribir " Muchas gracias por elegirnos"
	FinSi
FinProceso
