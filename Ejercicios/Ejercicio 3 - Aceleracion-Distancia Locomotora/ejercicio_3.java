/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "EJERCICIO_3.java."

import java.io.*;
import java.math.*;

public class ejercicio_3 {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		double v_aceleracion;
		double v_distancia;
		int v_tiempo;
		int v_velfin;
		double v_velini;
		// Programa que en base a la formula A=(VF-VI)/T - d=vi*t+1/2*a*t^2 calcula la aceleracion y distancia recorrida de una locomotora
		// Desarrollador: Carlos Manuel Muñoz
		// Fecha de Desarrollo: 20/02/2023
		// Version: 1.0
		// AREA DE DECLARAR VARIABLES, v_velini(VELOCIDADINICIAL), v_velfin(VELOCIDADFINAL), v_tiempo(TIEMPO), v_distancia(DISTANCIA), v_aceleracion(ACELERACION)
		// AREA DE ASIGNACION DE DATOS
		System.out.println("Ingrese la Velocidad Inicial:");
		v_velini = Double.parseDouble(bufEntrada.readLine());
		System.out.println("Ingrese la Velocidad Final:");
		v_velfin = Integer.parseInt(bufEntrada.readLine());
		System.out.println("Ingrese el Tiempo:");
		v_tiempo = Integer.parseInt(bufEntrada.readLine());
		// AREA DE OPERACIONES ARITMETICAS APLICANDO FORMULA A=(VF-VI)/T para ACELERACION
		v_aceleracion = (v_velfin-v_velini)/v_tiempo;
		// AREA DE OPERACIONES ARITMETICAS APLICANDO FORMULA D=VI*T+1/2*A*T^2 para DISTANCIA
		v_distancia = v_velini*v_tiempo+1/2*v_aceleracion*Math.pow(v_tiempo,2);
		// AREA DE RESULTADO DEL PROCESO ARITMETICO Y FIN DEL ALGORITMO
		System.out.println("La Aceleracion de la Locomotora es: "+v_aceleracion+"m/s");
		System.out.println("La Distancia recorrida por la Locomotora son: "+v_distancia+"m");
	}


}

