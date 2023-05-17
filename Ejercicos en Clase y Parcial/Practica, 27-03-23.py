# Analisis del primer parcial de FP

v_canEst = 0
c_valExaTeo = 0.40
v_proNotExaTeo = 0.0
v_sumNotExaTeo = 0.0
c_valExaPra = 0.60
v_proNotExaPra = 0.0
v_sumNotExaPra = 0.0
v_defPriPar = 0.0
v_conCic = 1
v_sumNotPriPar = 0.0
v_proNotPriPar = 0.0
v_acuSumDefEst = 0.0
v_notDefPriPar = 0.0

# Leer cantidad de estudiantes

v_canEst = int(input("Digite cantidad de estudiantes: "))

for v_conCic in range(v_canEst):

    # Captura de datos
    v_nomEst = input("Nombre Estudiante: ")
    v_genEst = input("Genero del Estudiante: ")
    v_notExaTeo = float(input("Digite Nota Examen Teorico: "))
    v_notExaPra = float(input("Digite Nota Examen Practico: "))

    # Calculo de la nota del primer parcial por estudiante
    v_notDefPriPar = v_notExaTeo * c_valExaTeo + v_notExaPra * c_valExaPra
    print("Su nota del Primer Parcial es: ", v_notDefPriPar)

    # Calcular la suma de las notas de los estudiantes para calcular el promedio 
    v_sumNotPriPar = v_sumNotPriPar + v_notDefPriPar

    # Calcular la suma de las notas de los estudiantes para calcular el promedio de las notas del examen teorico/practico
    v_sumNotExaTeo = v_sumNotExaTeo + v_notExaTeo
    v_sumNotExaPra = v_sumNotExaPra + v_notExaPra

    # Calcular el promedio por genero

    v_acuSumDefEst = v_acuSumDefEst + v_notDefPriPar

    if v_genEst == "F":
        v_acuSumDefEstMuj = v_acuSumDefEstMuj + v_notDefPriPar
        v_acuConEstMuj = v_acuConEstMuj + 1
    else:
        v_acuSumDefEstHom = v_acuSumDefEstHom + v_notDefPriPar
        v_acuConEstHom = v_acuConEstHom + 1


# Calcular el promedio del grupo de las notas de primer parcial
v_proNotPriPar = v_sumNotPriPar / v_canEst
print("El promedio del grupo del primer parcial es: ", v_proNotPriPar)

# Calcular el promedio del grupo de los examenes teoricos/practicos
v_proNotExaTeo = v_sumNotExaTeo/ v_canEst
print("El promedio del grupo de los Examenes Practicos es: ", v_proNotExaTeo)
v_proNotExaPra = v_sumNotExaPra/ v_canEst
print("El promedio del grupo de los Examenes Practicos es: ", v_proNotExaPra)

# Calculo de Promedio por genero
v_proNotDefEst = v_acuSumDefEst / v_canEst
v_proNotDefEstMuj = v_acuSumDefEstMuj / v_acuConEstMuj
v_proNotDefEstHom = v_acuSumDefEstHom / v_acuConEstHom