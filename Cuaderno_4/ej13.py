"""
Realizar un programa que lea palabras hasta que se introduzca “fin”, mostrando
un recuento de las longitudes de las palabras, es decir, el número total de
palabras de longitud 1 que se hayan introducido, el total de longitud 2, etc. La
máxima longitud de las palabras deberá ser de 15 caracteres. Una posible salida
de este programa sería:

Palabras longitud 1: ninguna
Palabras longitud 2: 10
…
Palabras longitud 15: 1
"""

def writer()->str:
    word = input('Dime una palabra: ')
    return word if len(word) < 15 else None

def showResult(arr):
    buffer = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    
    for i in range(len(arr)):
        l = len(arr[i])
        buffer[l].append(arr[i])
    
    for i in range(len(buffer)):
        print(f"Palabras longitud {i}: {'ninguna' if len(buffer[i]) == 0 else len(buffer[i])}")        
    
def UI():
    w = ''
    arr = []
    ok = False
    
    while not ok:
        w = writer()
        if(w == 'fin'):
            ok = True
            showResult(arr)
        elif(w == None):
            print("La palabra tiene que ser menor de 15 caracteres")
        else:
            arr.append(w)
UI()