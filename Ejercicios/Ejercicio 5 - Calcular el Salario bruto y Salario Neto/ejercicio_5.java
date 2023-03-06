/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "EJERCICIO_5.java."

import java.io.*;

public class ejercicio_5 {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		double bienestar_familiar;
		String cedula;
		String fecha_pago;
		double fondo_empleados;
		double horas_diurnas;
		double horas_nocturnas;
		double incremento_nocturno;
		String nombre;
		double retencion_fuente;
		double salario_base;
		double salario_bruto;
		double salario_neto;
		double salud_pension;
		double total_deducciones;
		double valor_hora;
		// Programa que calcula el salario de un empleado en base a las horas semanales y realiza las respectivas deducciones//
		// Desarrollador: Carlos Manuel Muñoz//
		// Fecha de Desarrollo: 21/02/2023//
		// Version: 1.0//
		// AREA DE DECLARACION DE VARIABLES
		// AREA DE ASIGNACION DE DATOS//
		System.out.println("Ingrese el nombre del empleado:");
		nombre = bufEntrada.readLine();
		System.out.println("Ingrese la cédula del empleado:");
		cedula = bufEntrada.readLine();
		System.out.println("Ingrese el valor de la hora del empleado:");
		valor_hora = Double.parseDouble(bufEntrada.readLine());
		System.out.println("Ingrese las horas diurnas trabajadas en la semana:");
		horas_diurnas = Double.parseDouble(bufEntrada.readLine());
		System.out.println("Ingrese las horas nocturnas trabajadas en la semana:");
		horas_nocturnas = Double.parseDouble(bufEntrada.readLine());
		System.out.println("Ingrese la fecha de pago (formato dd/mm/aaaa):");
		fecha_pago = bufEntrada.readLine();
		// AREA DEL CALCULO DE SALARIOBASE Y EXEDENTE NOCTURNO//
		salario_base = valor_hora*(horas_diurnas+horas_nocturnas);
		incremento_nocturno = valor_hora*0.4*horas_nocturnas;
		// AREA DE CALCULO DEL SALARIO BRUTO//
		salario_bruto = salario_base+incremento_nocturno;
		// AREA DEL CALCULO DE TODAS LAS DEDUCCIONES//
		retencion_fuente = salario_base*0.1;
		fondo_empleados = salario_base*0.03;
		bienestar_familiar = salario_base*0.02;
		salud_pension = salario_base*0.04;
		total_deducciones = retencion_fuente+fondo_empleados+bienestar_familiar+salud_pension;
		// AREA DE CALCULO DEL SALARIO NETO//
		salario_neto = salario_bruto-total_deducciones;
		// DESPRENDIBLE DE PAGO CON SUS RESPECTIVAS DEDUCCIONES Y FIN DEL ALGORITMO//
		System.out.println("--------------------------------------");
		System.out.println("          DESPRENDIBLE DE PAGO        ");
		System.out.println("--------------------------------------");
		System.out.println("Nombre: "+nombre);
		System.out.println("Cédula: "+cedula);
		System.out.println("Fecha de Pago: "+fecha_pago);
		System.out.println("--------------------------------------");
		System.out.println("Salario Base:"+salario_base);
		System.out.println("Incremento Nocturno:"+incremento_nocturno);
		System.out.println("Salario Bruto:"+salario_bruto);
		System.out.println("--------------------------------------");
		System.out.println("Retención en la Fuente:"+retencion_fuente);
		System.out.println("Fondo de Empleados:"+fondo_empleados);
		System.out.println("Bienestar Familiar:"+bienestar_familiar);
		System.out.println("Salud y Pensión:"+salud_pension);
		System.out.println("Total Deducciones:"+total_deducciones);
		System.out.println("--------------------------------------");
		System.out.println("Salario Neto:"+salario_neto);
		System.out.println("--------------------------------------");
	}


}

