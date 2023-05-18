Algoritmo CalculoNomina
		Definir horasTrabajadas, tarifaHora, salarioBruto, descuento, salarioNeto Como Real
		Definir opcion, numTrabajadores Como Entero
		Definir contador Como Entero
		contador <- 1
		
		Escribir "Ingrese el número de trabajadores:"
		Leer numTrabajadores
		
		Mientras contador <= numTrabajadores Hacer
			Escribir "Ingrese las horas trabajadas del trabajador ", contador, ":"
			Leer horasTrabajadas
			
			Escribir "Ingrese la tarifa por hora del trabajador ", contador, ":"
			Leer tarifaHora
			
			salarioBruto <- horasTrabajadas * tarifaHora
			
			Si salarioBruto > 1000 Entonces
				descuento <- salarioBruto * 0.1
			Sino
				descuento <- 0
			FinSi
			
			salarioNeto <- salarioBruto - descuento
			
			Escribir "El salario bruto del trabajador ", contador, " es: ", salarioBruto
			Escribir "El descuento aplicado es: ", descuento
			Escribir "El salario neto del trabajador ", contador, " es: ", salarioNeto
			Escribir ""
			
			contador <- contador + 1
		FinMientras
		

FinAlgoritmo
