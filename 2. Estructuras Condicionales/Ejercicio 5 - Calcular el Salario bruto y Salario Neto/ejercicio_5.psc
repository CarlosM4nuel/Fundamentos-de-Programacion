Algoritmo ejercicio_5
	//Programa que calcula el salario de un empleado en base a las horas semanales y realiza las respectivas deducciones//
	//Desarrollador: Carlos Manuel Muñoz//
	//Fecha de Desarrollo: 21/02/2023//
	//Version: 1.0//
	//AREA DE DECLARACION DE VARIABLES
	Definir valor_hora Como Real;
	Definir horas_diurnas Como Real;
	Definir horas_nocturnas Como Real;
	Definir salario_base Como Real;
	Definir salario_bruto Como Real;
	Definir salario_neto Como Real;
	Definir incremento_nocturno Como Real;
	Definir retencion_fuente Como Real;
	Definir fondo_empleados Como Real;
	Definir bienestar_familiar Como Real;
	Definir salud_pension Como Real;
	Definir total_deducciones Como Real;
	Definir cedula, nombre, fecha_pago Como Cadena
	
	//AREA DE ASIGNACION DE DATOS//
	Escribir "Ingrese el nombre del empleado:"; Leer nombre
	Escribir "Ingrese la cédula del empleado:"; Leer cedula
	Escribir "Ingrese el valor de la hora del empleado:"; Leer valor_hora
	Escribir "Ingrese las horas diurnas trabajadas en la semana:"; Leer horas_diurnas
	Escribir "Ingrese las horas nocturnas trabajadas en la semana:"; Leer horas_nocturnas
	Escribir "Ingrese la fecha de pago (formato dd/mm/aaaa):"; Leer fecha_pago
	
	//AREA DEL CALCULO DE SALARIOBASE Y EXEDENTE NOCTURNO//
	salario_base = valor_hora * (horas_diurnas + horas_nocturnas)
	incremento_nocturno = valor_hora * 0.4 * horas_nocturnas
	
	//AREA DE CALCULO DEL SALARIO BRUTO//
	salario_bruto = salario_base + incremento_nocturno
	
	//AREA DEL CALCULO DE TODAS LAS DEDUCCIONES//
	retencion_fuente = salario_base * 0.1
	fondo_empleados = salario_base * 0.03
	bienestar_familiar = salario_base * 0.02
	salud_pension = salario_base * 0.04
	total_deducciones = retencion_fuente + fondo_empleados + bienestar_familiar + salud_pension
	
	//AREA DE CALCULO DEL SALARIO NETO//
	salario_neto = salario_bruto - total_deducciones
	
	//DESPRENDIBLE DE PAGO CON SUS RESPECTIVAS DEDUCCIONES Y FIN DEL ALGORITMO//
	Escribir "--------------------------------------"
	Escribir "          DESPRENDIBLE DE PAGO        "
	Escribir "--------------------------------------"
	Escribir "Nombre: " nombre
	Escribir "Cédula: " cedula
	Escribir "Fecha de Pago: " fecha_pago
	Escribir "--------------------------------------"
	Escribir "Salario Base:" salario_base
	Escribir "Incremento Nocturno:" incremento_nocturno
	Escribir "Salario Bruto:" salario_bruto
	Escribir "--------------------------------------"
	Escribir "Retención en la Fuente:" retencion_fuente
	Escribir "Fondo de Empleados:" fondo_empleados
	Escribir "Bienestar Familiar:" bienestar_familiar
	Escribir "Salud y Pensión:" salud_pension
	Escribir "Total Deducciones:" total_deducciones
	Escribir "--------------------------------------"
	Escribir "Salario Neto:" salario_neto
	Escribir "--------------------------------------"
	
FinAlgoritmo
