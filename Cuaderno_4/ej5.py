"""
Modificar una lista de números reales que representan las calificaciones de los
alumnos de una clase, para sustituir los valores numéricos por sus calificaciones
alfanuméricas (Suspenso, Aprobado, etc.) 
"""
import random

nAlumnos = 20
notas = []
for i in range(nAlumnos):
    notas.append(random.randint(0,10))

print(notas)
for i in range(nAlumnos):
    if(notas[i] >= 5):
        notas[i] = 'AP'
    else:
        notas[i] = 'S'
print(notas)