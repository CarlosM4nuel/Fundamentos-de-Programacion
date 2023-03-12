Algoritmo sin_titulo
	//Area de documentacion
	//enunciado: Calculo del salario de empleados basados en las horas trabajadas
	//version: 1.0
	//desarrollado por: Carlos Manuel Muñoz
	//fecha: 23/02/2023
	
	//Area de definicion de variables
	Definir horas_trabajadas Como Real //Variable que va a almacenar las horas trabajadas del empleado
	Definir precio_hora Como Real //Variable que almacenara el precio de la hora trabajada
	Definir salario Como Real //Variable que almacenara el salario del empleado
	Definir nombre_empleado Como Cadena //Variable que almacera el nombre del empleado
	Definir mas_Datos Como Caracter //Variable para almacenar mas trabajadores en caso de continuar
	
	//Area de procesos y entrada de datos
	Repetir
		Escribir "Nombre del Empleado:"; leer nombre_empleado
		Escribir "Digite las Horas Trabajadas:"; Leer horas_trabajadas
		Escribir "Digite el Precio de la Hora"; Leer precio_hora
		si horas_trabajadas<=40 Entonces
			salario = horas_trabajadas * precio_hora
		SiNo
			salario = 40 * precio_hora + 1.5 * (horas_trabajadas-40) * precio_hora
		FinSi
		
		//Area de salidas
		Escribir "Empleado: " nombre_empleado
		Escribir "El Salario del Empleado: " nombre_empleado " es: " salario
		Escribir "¿Desea anotar otro trabajador?: "
		Leer mas_Datos
	Hasta Que mas_Datos =  "N"
FinAlgoritmo
