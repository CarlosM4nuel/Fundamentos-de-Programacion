Algoritmo ejercicio_6
	//Calcula la nota definitiva de un estudiante y lo aprueba o reprueba con la condicion que se asista x veces
	//Desarrollador: Carlos Manuel Muñoz
	//Fecha de Desarrollo: 25/02/2023
	//Version: 1.0
	//AREA DE DECLARACION DE VARIABLES
	Definir inasistencia Como Real
	Definir parcial_1 Como Real
	Definir parcial_2 Como Real
	Definir parcial_3 Como Real
	Definir p_p_1, p_p_2, p_p_3 Como Real
	Definir estudiante, materia Como Caracter
	
	//AREA DE CAPTURA DE DATOS
	Escribir " Digite su nombre "; Leer estudiante
	Escribir " Digite el nombre de la materia "; Leer materia
	Escribir 'Digite la nota del parcial 1 '; Leer parcial_1
	Escribir " Porcentaje parcial 1 "; Leer p_p_1
	Escribir ' Digite la nota del parcial 2 '; Leer parcial_2
	Escribir " Porcentaje parcial 2 "; Leer p_p_2
	Escribir ' Digite la nota del parcial 3 '; Leer parcial_3
	Escribir " Porcentaje parcial 3 "; Leer p_p_3
	Escribir ' Cuantas veces falto a clase '; Leer inasistencia
	
	//AREA DE PROCESOS 
	notas <- ((parcial_1/100)*p_p_1)+((parcial_2/100)*p_p_2)+((parcial_3/100)*p_p_3)
	Si inasistencia>12 Entonces
		Escribir "Reprobo por inasistencia"
	SiNo
		Escribir "Asistio cumplidamente"
		Si notas<3.4 Entonces
			Escribir "Reprobo"
		SiNo
			Escribir "Aprobo"
		FinSi
	FinSi
	
	//AREA DE SALIDAS
	Escribir "Su nota definitiva es: ", notas
FinAlgoritmo
