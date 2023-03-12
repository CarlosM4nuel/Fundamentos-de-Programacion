/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "EJERCICIO_4.java."

import java.io.*;

public class ejercicio_4 {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		int v_aceleracion;
		int v_tiempo;
		int v_transkmh_ms;
		int v_velfin;
		int v_velini;
		// Programa que en base a la formula T=(VF-VI)/A calcula el tiempo que demora en llegar a 144km/h//
		// Desarrollador: Carlos Manuel Muñoz//
		// Fecha de Desarrollo: 20/02/2023//
		// Version: 1.0//
		// AREA DE DEFINICION DE VARIABLES, VI(VELOCIDADINICIAL), VF(VELOCIDADFINAL), A(ACELERACION), T(TIEMPO), M(CAMBIO DE KM/H->M/S//
		// AREA DE ASIGNACION DE DATOS//
		System.out.println("Digite la Velocidad Inicial");
		v_velini = Integer.parseInt(bufEntrada.readLine());
		System.out.println("Digite la Velocidad Final");
		v_velfin = Integer.parseInt(bufEntrada.readLine());
		System.out.println("Digite la Aceleracion");
		v_aceleracion = Integer.parseInt(bufEntrada.readLine());
		// AREA DE OPERACIONES ARITMETICAS APLICANDO FORMULA M=(VF*1000)/3600 para TRANSFORMAR KM/H -> M/S//
		v_transkmh_ms = v_velfin*(1000/3600);
		// AREA DE OPERACIONES ARITMETICAS APLICANDO FORMULA T=(VF-VI)/A para ACELERACION//
		v_tiempo = (v_transkmh_ms-v_velini)/v_aceleracion;
		// AREA DE RESULTADO DEL PROCESO ARITMETICO Y FIN DEL ALGORITMO//
		System.out.println("El tiempo que tarda es: "+v_tiempo+" Segundos");
	}


}

