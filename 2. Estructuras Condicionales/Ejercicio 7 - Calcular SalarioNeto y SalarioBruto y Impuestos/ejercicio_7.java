/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "CALCULO_SALARIO.java."

import java.io.*;

public class calculo_salario {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		double horas_trabajadas;
		double impuestos;
		String nombre_empleado;
		double precio_hora;
		double salario_bruto;
		double salario_neto;
		// Area de documentacion
		// enunciado: Calculo del Salario Bruto y Salario Neto en base a la horas trabajadas restandole los impuestos a pagar
		// version: 1.0
		// desarrollado por: Carlos Manuel Muñoz
		// fecha: 24/02/2023
		// Area de definicion de variables
		// Variable que almacenara las horas semanales trabajadas por X empleado
		// Variable que almacenara el valor de la hora de trabajo de X empleado
		// Variable que almacenara el nombre del empleado a realizar el proceso
		// Area de entradas
		System.out.println("Digite el Nombre del Empleado");
		nombre_empleado = bufEntrada.readLine();
		System.out.println("Digite las Horas Trabajadas");
		horas_trabajadas = Double.parseDouble(bufEntrada.readLine());
		System.out.println("Digite el Precio de la Hora");
		precio_hora = Double.parseDouble(bufEntrada.readLine());
		// Area de procesos
		salario_bruto = horas_trabajadas*precio_hora;
		impuestos = 0.25*salario_bruto;
		salario_neto = salario_bruto-impuestos;
		// Area de salidas
		System.out.println("Nombre del Empleado: "+nombre_empleado);
		System.out.println("Las Horas Trabajadas por "+nombre_empleado+" son: "+horas_trabajadas);
		System.out.println("Los Impuestos a Descontar son: "+impuestos);
		System.out.println("Su Salario Bruto es: "+salario_bruto);
		System.out.println("Su Salario Neto es: "+salario_neto);
	}


}

