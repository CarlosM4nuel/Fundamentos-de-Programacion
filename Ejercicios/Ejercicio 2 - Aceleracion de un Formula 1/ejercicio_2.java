/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "EJERCICIO_2.java."

import java.io.*;

public class ejercicio_2 {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		double aceleracion;
		int v_tiempo;
		int v_transkm_ms;
		int v_velfin;
		int v_velini;
		// Programa que en base a la formula A=(VF-VI)/T calcula la aceleracion de un formula 1//
		// Desarrollador: Carlos Manuel Muñoz//
		// Fecha de Desarrollo: 20/02/2023//
		// Version: 1.0//
		// AREA DE DEFINICION DE VARIABLES, v_velIni(VELOCIDADINICIAL), v_velFin(VELOCIDADFINAL), v_Tiempo(TIEMPO), aceleracion(ACELERACION)//
		// AREA DE ASIGNACION DE DATOS//
		System.out.println("Digite la velocidad Inicial");
		v_velini = Integer.parseInt(bufEntrada.readLine());
		System.out.println("Digite la velocidad Final");
		v_velfin = Integer.parseInt(bufEntrada.readLine());
		System.out.println("Digite el Tiempo");
		v_tiempo = Integer.parseInt(bufEntrada.readLine());
		// AREA DE TRANSFORMACION DE KM/H -> M/S FORMULA: VF*1000/3600//
		v_transkm_ms = (v_velfin*1000)/3600;
		// AREA DE OPERACIONES ARITMETICAS APLICANDO FORMULA A=(VF-VI)/T//
		aceleracion = (v_transkm_ms-v_velini)/v_tiempo;
		// AREA DE RESULTADO DEL PROCESO ARITMETICO Y FIN DEL ALGORITMO//
		System.out.println("La aceleracion es: "+aceleracion+" m/s2");
	}


}

