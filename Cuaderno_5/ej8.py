def ask():
    matriz = []
    fila = []
    for filas in range(3):
        for columnas in range(4):
            n = int(input(f'Introduce el elemento {filas}x{columnas} '))
            fila.append(n)
        matriz.append(fila)
        fila = []

    return matriz

def suma():
    a = ask()
    b = ask()
    
    for fila in range(len(a)):
        for columna in range(len(a[0])):
            print(a[fila][columna] + b[fila][columna], end=" ")
        print()
        print()
suma()