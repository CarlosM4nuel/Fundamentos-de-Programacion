Algoritmo DiaSemana
    Definir dia, mes, anio Como Entero
    Definir fechaTexto Como Caracter
    Definir diaSemana Como Caracter
    
    Escribir "Ingrese la fecha en formato DD/MM/AAAA:"
    Leer fechaTexto
    
    dia <- ConvertirASubcadena(1, 2, fechaTexto)
    mes <- ConvertirASubcadena(4, 5, fechaTexto)
    anio <- ConvertirASubcadena(7, 10, fechaTexto)
    
    // Validar que la fecha ingresada sea válida
    Mientras dia <= 0 O dia > 31 O mes <= 0 O mes > 12 O anio <= 0 Hacer
        Escribir "Fecha inválida. Vuelva a ingresar la fecha:"
        Leer fechaTexto
        
        dia <- ConvertirASubcadena(1, 2, fechaTexto)
        mes <- ConvertirASubcadena(4, 5, fechaTexto)
        anio <- ConvertirASubcadena(7, 10, fechaTexto)
    FinMientras
    
    // Cálculo del día de la semana usando la fórmula de Zeller
    Si mes < 3 Entonces
        mes <- mes + 12
        anio <- anio - 1
    FinSi
    
    Definir a, b, c, d, f Como Entero
    a <- anio / 100
    b <- a / 4
    c <- 2 - a + b
    d <- dia + ((31 * (mes + 1)) / 12) + anio + (anio / 4) - c
    f <- d % 7
    
    // Asignar el nombre del día de la semana correspondiente
    Segun f Hacer
			Caso 0
            diaSemana <- "Sábado"
			Caso 1
            diaSemana <- "Domingo"
			Caso 2
            diaSemana <- "Lunes"
			Caso 3
            diaSemana <- "Martes"
			Caso 4
            diaSemana <- "Miércoles"
			Caso 5
            diaSemana <- "Jueves"
			Caso 6
            diaSemana <- "Viernes"
    FinSegun
    
    Escribir "El ", fechaTexto, " es ", diaSemana
FinAlgoritmo

