# -*- coding: utf-8 -*-
"""Copia de Te damos la bienvenida a Colaboratory

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gZphY7i_nm5pQ93wT_gx2Obs_o-AzhaS
"""

import random
lista = []
longitud = 30
for x in range(longitud):
  lista.append(random.randint(0,30))
print(lista)

import random
lista = []
longitud = 30
for x in range (longitud):
  lista.append(random.randint(0,30))
print(lista)
valor = int(input("Digite un valor: "))
for i in range(longitud):
  if lista[i]==valor:
    lista[i]=-1
print(lista)

import random
lista = []
longitud = 30
for x in range (longitud):
  lista.append(random.randint(0,30))
print(lista)
valor = int(input("Digite un valor: "))
for i in range(longitud):
  if lista[i]==valor:
    lista[i]=-1
print(lista)
num = int(input("Numero a eliminar: "))
lista.remove(num)
print(lista)

import random
lista = []
longitud = 30
for x in range (longitud):
  lista.append(random.randint(0,30))
print(lista)
valor = int(input("Digite un valor: "))
for i in range(longitud):
  if lista[i]==valor:
    lista[i]=-1
print(lista)
num = int(input("Numero a eliminar: "))
lista.remove(num)
print(lista)
val = int(input("Digite un valor: "))
lista.append(val)
lista.sort()
print(lista)

num = int(input("Ingrese un número: "))
lista = [int(x) for x in input("Ingrese una lista de números separados por espacios: ").split()]

contador = 0
for x in lista:
    if x == num:
        contador += 1

print("El número que se repite en la lista es ", num, contador)

#Lista Aleatoria, Lista ordenada, lista de repeticiones
import random
lista_aleatorea = []
longitud = 5
for x in range (longitud):
  lista_aleatorea.append(random.randint(0,5))
print(lista_aleatorea)

#Ordenar la lista
lista_aleatorea.sort()
print(lista_aleatorea)

#Cuanto se repite
lista_aleatorea.count()
print(lista_aleatorea)

#Gestor de Notas, Listas de Estudiastes-Edades-NotaFinalProgra-Inasistencias
import random
listEst = []
listEdad = []
listNotFinPro = []
listInas = []
longitud = 5
for x in range (longitud):
  lista.append(random.randint(0,5))
print(lista)