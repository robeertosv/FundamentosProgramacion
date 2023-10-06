"""
Una universidad acaba de modificar su sistema de representación de la calificación
de los alumnos. A partir de ahora, se calificarán como “A” las notas mayores o
iguales a 8,5, “B” las mayores o iguales a 6,5, “C” las calificaciones mayores o
iguales a 5, “D” las calificaciones mayores o iguales a 3,5, y “F” todas las demás.

Programa una función que reciba una calificación numérica y retorne la letra con la
nueva calificación, luego pruébala con valores introducidos por el usuario. Tal vez
sea buena idea basarte en el ejercicio resuelto número 1 pero, a diferencia de lo
que se hace allí (se controla la validez con una precondición), asegúrate de que la
calificación introducida es válida.

"""

def conversor(nota:float)->str:
    n = None
    
    if(nota >= 8.5):
        n = "A"
    elif(nota >= 6.5 and nota < 8.5):
        n = 'B'
    elif(nota < 6.5 and nota >= 5):
        n = 'C'
    elif(nota < 5 and nota >= 3.5):
        n = 'D'
    else:
        n = 'F'
    
    return n

nota = float(input("Introduce la nota: "))

print(conversor(nota))