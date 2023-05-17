lista = []
for x in range(5):
    valor=int(input("Ingrese un valor:"))
    lista.append(valor)
print(lista)

mayor=lista[0]
for x in range(1,5):
    if lista[x]>mayor:
        mayor=lista[x]
menor=mayor
for x in range(0,5):
    if lista[x]<menor:
        menor=lista[x]

print("PEDIR UN DATO Y BUSCARLO")
valbus=int(input(""))

poslis=0
canelerep=0
while poslis<int(len(lista)):
    if lista[poslis]==valbus:
        canelerep=canelerep+1
        lisposrep.append(poslis)

print("Lista Completa")
print(lista)
print("Mayor de la Lista")
print(mayor)
print("Menor de la lista")
print(menor)

#leer un numero por teclado, 
#si esta o no esta?
#cuantas veces se repite y en q posiciones?


