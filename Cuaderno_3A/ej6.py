"""
Escribe un algoritmo que tras leer tres enteros los escriba en pantalla en orden
creciente. Como siempre, valida las entradas.

"""

n1 = int(input("Introduce un número: "))
n2 = int(input("Introduce un número: "))
n3 = int(input("Introduce un número: "))

a = [n1, n2, n3]
a.sort()

print(a)