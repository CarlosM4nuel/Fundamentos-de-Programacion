Algoritmo EncontrarMaximo
    Definir A, B, C como Entero
    Definir Maximo como Entero
	
    Escribir "Ingrese el valor de A:"
    Leer A
	
    Escribir "Ingrese el valor de B:"
    Leer B
	
    Escribir "Ingrese el valor de C:"
    Leer C
	
    Maximo <- A  // Asignamos el valor de A como m�ximo inicialmente
	
    Si B > Maximo Entonces
        Maximo <- B
    Fin Si
	
    Si C > Maximo Entonces
        Maximo <- C
    Fin Si
	
    Escribir "El n�mero m�s grande es:", Maximo
	
FinAlgoritmo
