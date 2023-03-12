/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "EJERCICIO_6.java."

import java.io.*;

public class ejercicio_6 {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		String estudiante;
		double inasistencia;
		String materia;
		double notas;
		double parcial_1;
		double parcial_2;
		double parcial_3;
		double p_p_1;
		double p_p_2;
		double p_p_3;
		// Calcula la nota definitiva de un estudiante y lo aprueba o reprueba con la condicion que se asista x veces
		// Desarrollador: Carlos Manuel Muñoz
		// Fecha de Desarrollo: 25/02/2023
		// Version: 1.0
		// AREA DE DECLARACION DE VARIABLES
		// AREA DE CAPTURA DE DATOS
		System.out.println(" Digite su nombre ");
		estudiante = bufEntrada.readLine();
		System.out.println(" Digite el nombre de la materia ");
		materia = bufEntrada.readLine();
		System.out.println("Digite la nota del parcial 1 ");
		parcial_1 = Double.parseDouble(bufEntrada.readLine());
		System.out.println(" Porcentaje parcial 1 ");
		p_p_1 = Double.parseDouble(bufEntrada.readLine());
		System.out.println(" Digite la nota del parcial 2 ");
		parcial_2 = Double.parseDouble(bufEntrada.readLine());
		System.out.println(" Porcentaje parcial 2 ");
		p_p_2 = Double.parseDouble(bufEntrada.readLine());
		System.out.println(" Digite la nota del parcial 3 ");
		parcial_3 = Double.parseDouble(bufEntrada.readLine());
		System.out.println(" Porcentaje parcial 3 ");
		p_p_3 = Double.parseDouble(bufEntrada.readLine());
		System.out.println(" Cuantas veces falto a clase ");
		inasistencia = Double.parseDouble(bufEntrada.readLine());
		// AREA DE PROCESOS 
		notas = ((parcial_1/100)*p_p_1)+((parcial_2/100)*p_p_2)+((parcial_3/100)*p_p_3);
		if (inasistencia>12) {
			System.out.println("Reprobo por inasistencia");
		} else {
			System.out.println("Asistio cumplidamente");
			if (notas<3.4) {
				System.out.println("Reprobo");
			} else {
				System.out.println("Aprobo");
			}
		}
		// AREA DE SALIDAS
		System.out.println("Su nota definitiva es: "+notas);
	}


}

