# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Programa que calcula el salario de un empleado en base a las horas semanales y realiza las respectivas deducciones//
	# Desarrollador: Carlos Manuel Muoz//
	# Fecha de Desarrollo: 21/02/2023//
	# Version: 1.0//
	# AREA DE DECLARACION DE VARIABLES
	valor_hora = float()
	horas_diurnas = float()
	horas_nocturnas = float()
	salario_base = float()
	salario_bruto = float()
	salario_neto = float()
	incremento_nocturno = float()
	retencion_fuente = float()
	fondo_empleados = float()
	bienestar_familiar = float()
	salud_pension = float()
	total_deducciones = float()
	cedula = str()
	nombre = str()
	fecha_pago = str()
	# AREA DE ASIGNACION DE DATOS//
	print("Ingrese el nombre del empleado:")
	nombre = input()
	print("Ingrese la cedula del empleado:")
	cedula = input()
	print("Ingrese el valor de la hora del empleado:")
	valor_hora = float(input())
	print("Ingrese las horas diurnas trabajadas en la semana:")
	horas_diurnas = float(input())
	print("Ingrese las horas nocturnas trabajadas en la semana:")
	horas_nocturnas = float(input())
	print("Ingrese la fecha de pago (formato dd/mm/aaaa):")
	fecha_pago = input()
	# AREA DEL CALCULO DE SALARIOBASE Y EXEDENTE NOCTURNO//
	salario_base = valor_hora*(horas_diurnas+horas_nocturnas)
	incremento_nocturno = valor_hora*0.4*horas_nocturnas
	# AREA DE CALCULO DEL SALARIO BRUTO//
	salario_bruto = salario_base+incremento_nocturno
	# AREA DEL CALCULO DE TODAS LAS DEDUCCIONES//
	retencion_fuente = salario_base*0.1
	fondo_empleados = salario_base*0.03
	bienestar_familiar = salario_base*0.02
	salud_pension = salario_base*0.04
	total_deducciones = retencion_fuente+fondo_empleados+bienestar_familiar+salud_pension
	# AREA DE CALCULO DEL SALARIO NETO//
	salario_neto = salario_bruto-total_deducciones
	# DESPRENDIBLE DE PAGO CON SUS RESPECTIVAS DEDUCCIONES Y FIN DEL ALGORITMO//
	print("--------------------------------------")
	print("          DESPRENDIBLE DE PAGO        ")
	print("--------------------------------------")
	print("Nombre: ",nombre)
	print("Cedula: ",cedula)
	print("Fecha de Pago: ",fecha_pago)
	print("--------------------------------------")
	print("Salario Base:",salario_base)
	print("Incremento Nocturno:",incremento_nocturno)
	print("Salario Bruto:",salario_bruto)
	print("--------------------------------------")
	print("Retencion en la Fuente:",retencion_fuente)
	print("Fondo de Empleados:",fondo_empleados)
	print("Bienestar Familiar:",bienestar_familiar)
	print("Salud y Pension:",salud_pension)
	print("Total Deducciones:",total_deducciones)
	print("--------------------------------------")
	print("Salario Neto:",salario_neto)
	print("--------------------------------------")

