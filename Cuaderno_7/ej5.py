"""
Haz un programa para gestionar las notas de una clase de 20 alumnos de los
cuales sabemos su nombre y la nota obtenida. El programa debe permitir:
a. Introducir los datos de los alumnos por teclado.
b. Dado un nombre de un alumno, buscarlo y modificar su nota,
mostrando el resultado por pantalla (empleando búsqueda secuencial).
c. Dado un nombre de un alumno, buscarlo y mostrar la información por
pantalla empleando búsqueda binaria.
d. Realizar la media de todas las notas.
e. Realizar la media de las notas superiores o iguales a 5.
f. Realizar la ordenación (método de selección) de los alumnos por notas
en orden descendente y mostrar la nota del alumno con mejor nota.
g. Utilizando el método de inserción, realizar la ordenación de los alumnos
por notas en orden ascendente y mostrar la nota del alumno que peor
nota haya sacado.
"""

clase = [
    {
        'nombre': 'Roberto Seco',
        'nota': 10
    },
    {
        'nombre': 'Juan Perez',
        'nota': 5
    },
    {
        'nombre': 'Maria Garcia',
        'nota': 8
    },
    {
        'nombre': 'Laura Lopez',
        'nota': 3
    },
    {
        'nombre': 'Sara Fernandez',
        'nota': 7
    },
    {
        'nombre': 'Josefa Sanchez',
        'nota': 6
    },
    {
        'nombre': 'Pedro Martinez',
        'nota': 9
    },
    {
        'nombre': 'Antonio Jimenez',
        'nota': 4
    },
    {
        'nombre': 'Manuel Ruiz',
        'nota': 2
    },
    {
        'nombre': 'Raul Gonzalez',
        'nota': 1
    },
    {
        'nombre': 'Roberto García',
        'nota': 5
    },
    {
        'nombre': 'Juan Perez',
        'nota': 5
    },
    {
        'nombre': 'Maria Garcia',
        'nota': 8
    },
    {
        'nombre': 'Laura Lopez',
        'nota': 3
    },
    {
        'nombre': 'Sara Fernandez',
        'nota': 7
    },
    {
        'nombre': 'Josefa Sanchez',
        'nota': 6
    },
    {
        'nombre': 'Pedro Martinez',
        'nota': 9
    },
    {
        'nombre': 'Antonio Jimenez',
        'nota': 4
    },
    {
        'nombre': 'Manuel Ruiz',
        'nota': 2
    },
    {
        'nombre': 'Raul Gonzalez',
        'nota': 1
    }
]

def insertData(clase:list):
    for i in range(20):
        name = input("Introduce el nombre del alumno: ")
        nota= float(input('Introduce la nota el alumno: '))
        
        clase.append({'nombre': name, 'nota': nota})
        
def changeNota(clase:list, name:str, nota:float):
    i = 0
    found = False
    
    while not found and i < len(clase):
        if clase[i]['nombre'] == name:
            found = True
        else:
            i+=1
    clase[i]['nota'] = nota
    print(f'{name} ahora tiene un {clase[i]["nota"]}')
    
changeNota(clase, 'Josefa Sanchez', 8)

def showData(clase:list, name:str):
    # 1º habrá que ordenar a los alumnos por orden alfabético del nombre (bubble sort por simplicidad)
    n = len(clase) - 1
    
    for i in range(n):
        for j in range(n-i):
            if clase[j+1]['nombre'] < clase[j]['nombre']:
                clase[j+1], clase[j] = clase[j], clase[j+1]
    
    # Aplicar la búsqueda binaria
    
    found = False
    idx = len(clase) // 2
    i = 0
    
    while not found and i < len(clase):
        if clase[idx]['nombre'] == name:
            found = True
        elif clase[idx]['nombre'] < name:
            idx += len(clase[idx:len(clase)]) // 2
            i +=1
        else:
            idx //= 2
            i+=1

    return f"Nombre: {name}\nNota: {clase[idx]['nota']}" if found else f'No existe el alumno {name}'

#print(showData(clase, 'Roberto Seco'))

def meanAll(clase):
    sumatorio = 0
    n = len(clase)
    for i in range(len(clase)):
        sumatorio += clase[i]['nota']
    
    return sumatorio / n

def meanAprobados(clase):
    sumatorio = 0
    n = 0
    
    for i in range(len(clase)):
        if clase[i]['nota'] >= 5:
            n += 1
            sumatorio += clase[i]['nota']
    return sumatorio / n

def dSort(clase):
    for i in range(len(clase)):
        min_idx = i
        
        for j in range(i+1, len(clase)):
            if clase[min_idx]['nota'] < clase[j]['nota']:
                min_idx = j
        clase[i], clase[min_idx] = clase[min_idx], clase[i]
    
    print(f"la mejor nota la tiene {clase[0]['nombre']}, que ha sacado un {clase[0]['nota']}")
    
def aSort(clase):
    for i in range(len(clase)):
        key = clase[i]['nota']
        j = i-1
        
        while j >= 0 and key < clase[j]['nota']:
            clase[j], clase[j+1] = clase[j+1], clase[j]
            j-=1
        clase[j+1]['nota'] = key
    
    print(f"La peor nota la tiene {clase[0]['nombre']}, que ha sacado un {clase[0]['nota']}")

aSort(clase)