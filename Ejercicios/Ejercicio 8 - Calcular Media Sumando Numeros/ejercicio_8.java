/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "SIN_TITULO.java."

import java.io.*;

public class sin_titulo {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		int contador_numeros;
		double media;
		double num;
		double suma_numeros;
		// Area de documentacion
		// enunciado: Calcular la media de una serie de números positivos
		// version: 1.0
		// desarrollado por: Carlos Manuel Muñoz
		// fecha: 23/02/2023
		// Area de definicion de variables
		// Variable que almacenara los numeros digitados e ira sumandoles 1
		// Variable que ira sumando los numeros digitados
		// Area de entradas
		System.out.println("Digite los numeros:  (Para finalizar el proceso introduce 0)");
		do {
			num = Double.parseDouble(bufEntrada.readLine());
			if (num!=0) {
				// Area de procesos
				contador_numeros = contador_numeros+1;
				// Area de procesos
				suma_numeros = suma_numeros+num;
			}
		} while (num!=0);
		// Area de procesos
		if ((contador_numeros>0)) {
			// Area de procesos
			media = suma_numeros/contador_numeros;
			// Area de salidas
			System.out.println("La Media es: "+media);
		}
	}


}

