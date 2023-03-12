/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "SIN_TITULO.java."

import java.io.*;

public class sin_titulo {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		double horas_trabajadas;
		String mas_datos;
		String nombre_empleado;
		double precio_hora;
		double salario;
		// Area de documentacion
		// enunciado: Calculo del salario de empleados basados en las horas trabajadas
		// version: 1.0
		// desarrollado por: Carlos Manuel Muñoz
		// fecha: 23/02/2023
		// Area de definicion de variables
		// Variable que va a almacenar las horas trabajadas del empleado
		// Variable que almacenara el precio de la hora trabajada
		// Variable que almacenara el salario del empleado
		// Variable que almacera el nombre del empleado
		// Variable para almacenar mas trabajadores en caso de continuar
		// Area de procesos y entrada de datos
		do {
			System.out.println("Nombre del Empleado:");
			nombre_empleado = bufEntrada.readLine();
			System.out.println("Digite las Horas Trabajadas:");
			horas_trabajadas = Double.parseDouble(bufEntrada.readLine());
			System.out.println("Digite el Precio de la Hora");
			precio_hora = Double.parseDouble(bufEntrada.readLine());
			if (horas_trabajadas<=40) {
				salario = horas_trabajadas*precio_hora;
			} else {
				salario = 40*precio_hora+1.5*(horas_trabajadas-40)*precio_hora;
			}
			// Area de salidas
			System.out.println("Empleado: "+nombre_empleado);
			System.out.println("El Salario del Empleado: "+nombre_empleado+" es: "+salario);
			System.out.println("¿Desea anotar otro trabajador?: ");
			mas_datos = bufEntrada.readLine();
		} while (!mas_datos.equals("N"));
	}


}

