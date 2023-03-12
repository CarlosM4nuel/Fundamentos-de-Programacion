/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "SIN_TITULO.java."

import java.io.*;

public class sin_titulo {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		double fact;
		double n;
		double n_pasos;
		// Area de documentacion
		// enunciado: Determinacion de la cantidad total a pagar por una llamada telefonica
		// version: 1.0
		// desarrollado por: Carlos Manuel Muñoz
		// fecha: 23/02/2023
		// Area de definicion de variables
		// Variable que almacena el numero de pasos de la llamada
		// Area de entrada de datos
		System.out.println("Ingrese el numero de pasos de la llamada: ");
		n_pasos = Double.parseDouble(bufEntrada.readLine());
		// Area de procesos
		if (n_pasos<=0) {
			System.out.println("NO SE PUEDE REALIZAR ESTA ACCION");
		} else {
			fact = 10;
			n = n_pasos-5;
			if (n>0) {
				fact = fact+n*5;
			} else {
			}
		}
		// Area de salidas
		System.out.println("Numero de pasos de la llamada: "+n_pasos);
		System.out.println("El Precio de la llamada es: "+fact);
		System.out.println("Número de pasos que exceden a 5: "+n);
	}


}

