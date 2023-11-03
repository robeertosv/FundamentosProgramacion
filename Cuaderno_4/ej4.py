"""
Crear una lista de enteros, inicializarlos según valores aleatorios en el rango 1..20
y computar la media de los valores, el valor más alto y el más bajo (todo ello
utilizando listas). 
"""
import random

lista = []

for i in range(10):
    lista.append(random.randint(1,20))

media = sum(lista) / len(lista)
maximo = max(lista)
minimo = min(lista)

print(lista, media, maximo, minimo)