def mostrar_mayor(v1,v2,v3):
    print("El valor mayor de los tres numeros es")
    if v1>v2 and v1>v3:
        print(v1)
    else:
        if v2>v3:
            print(v2)
        else:
            print(v3)

def mostrar_menor(v1,v2,v3):
    print("El valor menor de los tres numeros es")
    if v1<v2 and v1<v3:
        print(v1)
    else:
        if v2<v3:
            print(v2)
        else:
            print(v3)

def ordenar_mayor(v1,v2,v3):
    print("Numeros ordenados de mayor a menor")
    for i in list:
         for j in range(len(list) - 1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

def cargar():
    valor1=int(input("Ingrese el primer valor:"))
    valor2=int(input("Ingrese el segundo valor:"))
    valor3=int(input("Ingrese el tercer valor:"))
    mostrar_mayor(valor1,valor2,valor3)
    mostrar_menor(valor1,valor2,valor3)
    ordenar_mayor(valor1,valor2,valor3)

cargar()

# Def = Definicion de una funcion
# 1. Declaracion                    Funciones con parametros y sin parametros, def(palabra reservada)
# 2. Desarrollo del codigo          
# 3. Llamado de la funcion          