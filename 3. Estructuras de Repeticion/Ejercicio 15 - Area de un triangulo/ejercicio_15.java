/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "EJERCICIO_15.java."

import java.io.*;
import java.math.*;

public class ejercicio_15 {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		double area;
		double lado1;
		double lado2;
		double lado3;
		double perimetro;
		double semiperimetro;
		// Programa que nos calcule el área de un triángulo conociendo sus lados
		// control de la entrada de datos en el programa.//
		// desarrolado por: Carlos Manuel Muñoz Muñoz
		// version 1.0//
		// fecha ultima actualización 9/03/2023//
		// AREA DEFINICION DE VARIABLES//
		// INICIAZION DE VARIABLES//
		lado1 = 0.0;
		lado2 = 0.0;
		lado3 = 0.0;
		// AREA DE ENTRADAS//
		System.out.println(" Digite el valor del primer lado: ");
		lado1 = Double.parseDouble(bufEntrada.readLine());
		System.out.println(" Digite el valor del segundo lado: ");
		lado2 = Double.parseDouble(bufEntrada.readLine());
		System.out.println(" Digite el valor del tercer lado: ");
		lado3 = Double.parseDouble(bufEntrada.readLine());
		// AREA DE PROCESOS//
		perimetro = lado1+lado2+lado3;
		System.out.println(" El perimetro es: "+perimetro);
		semiperimetro = perimetro/2;
		System.out.println(" El Semiperimetro es: "+semiperimetro);
		area = Math.sqrt(semiperimetro*(semiperimetro-lado1)*(semiperimetro-lado2)*(semiperimetro-lado3));
		System.out.println(" El Area del triangulo es: "+area);
	}


}

