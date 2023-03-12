# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).

from math import sqrt

if __name__ == '__main__':
	# Programa que nos calcule el área de un triángulo conociendo sus lados
	# control de la entrada de datos en el programa.//
	# desarrolado por: Carlos Manuel Muñoz Muñoz
	# version 1.0//
	# fecha ultima actualización 9/03/2023//
	# AREA DEFINICION DE VARIABLES//
	lado1 = float()
	lado2 = float()
	lado3 = float()
	# INICIAZION DE VARIABLES//
	lado1 = 0.0
	lado2 = 0.0
	lado3 = 0.0
	# AREA DE ENTRADAS//
	print(" Digite el valor del primer lado: ")
	lado1 = float(input())
	print(" Digite el valor del segundo lado: ")
	lado2 = float(input())
	print(" Digite el valor del tercer lado: ")
	lado3 = float(input())
	# AREA DE PROCESOS//
	perimetro = lado1+lado2+lado3
	print(" El perimetro es: ",perimetro)
	semiperimetro = perimetro/2
	print(" El Semiperimetro es: ",semiperimetro)
	area = sqrt(semiperimetro*(semiperimetro-lado1)*(semiperimetro-lado2)*(semiperimetro-lado3))
	print(" El Area del triangulo es: ",area)

