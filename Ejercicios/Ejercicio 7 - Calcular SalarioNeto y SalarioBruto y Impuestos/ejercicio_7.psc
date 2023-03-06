Algoritmo calculo_salario
	//Area de documentacion
	//enunciado: Calculo del Salario Bruto y Salario Neto en base a la horas trabajadas restandole los impuestos a pagar
	//version: 1.0
	//desarrollado por: Carlos Manuel Muñoz
	//fecha: 24/02/2023
	
	//Area de definicion de variables
	Definir horas_trabajadas Como Real //Variable que almacenara las horas semanales trabajadas por X empleado
	Definir precio_hora Como Real //Variable que almacenara el valor de la hora de trabajo de X empleado
	Definir nombre_empleado Como Caracter //Variable que almacenara el nombre del empleado a realizar el proceso
	
	//Area de entradas
	Escribir "Digite el Nombre del Empleado"; leer nombre_empleado
	Escribir "Digite las Horas Trabajadas"; leer horas_trabajadas
	Escribir "Digite el Precio de la Hora"; leer precio_hora
	
	//Area de procesos
	salario_bruto = horas_trabajadas * precio_hora
	impuestos = 0.25 * salario_bruto
	salario_neto = salario_bruto - impuestos
	
	//Area de salidas
	Escribir "Nombre del Empleado: " nombre_empleado
	Escribir "Las Horas Trabajadas por " nombre_empleado " son: " horas_trabajadas
	Escribir "Los Impuestos a Descontar son: " impuestos
	Escribir "Su Salario Bruto es: " salario_bruto
	Escribir "Su Salario Neto es: " salario_neto
FinAlgoritmo
